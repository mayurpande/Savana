import os

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse

from converter.models import PatientData
from functional_tests.test_pdf_to_text_converter_page import PDF_FILE


# Create your tests here.
from functional_tests.test_txt_file_to_json_converter import TXT_FILE


class RouteTemplateTester(TestCase):

    def route(self, path, template_name):
        self.path = path
        self.template_name = template_name
        response = self.client.get(self.path)
        self.assertTemplateUsed(response, self.template_name)


class HomePageTest(RouteTemplateTester):

    def test_home_page_returns_template(self):

        self.route(reverse('index'), 'home.html')


class PdfConverterTest(RouteTemplateTester):

    """Test cases for PdfConverter"""

    def setUp(self):

        """Opens Static pdf file for testing and uses the client to post form data"""

        with open(PDF_FILE, 'rb') as f:
            upload_file = f.read()
            form_data = {'title': 'test title', 'file': SimpleUploadedFile(f.name, upload_file)}
            self.response = self.client.post(reverse('pdf'), form_data)

    def tearDown(self):

        """Removes all files in MEDIA_ROOT directory once test is completed"""

        [os.remove(os.path.join(settings.MEDIA_ROOT, x)) for x in os.listdir(settings.MEDIA_ROOT)]

    def test_pdf_converter_page_returns_template(self):

        """Assert template is used"""

        self.route(reverse('pdf'), 'pdf.html')

    def test_POST_form_saves_file_as_pdf(self):

        """Asserts pdf file is exists (after being saved from handle_upload_file)"""

        self.assertEqual(os.path.exists(os.path.join(settings.MEDIA_ROOT, "Report1.pdf")), True)

    def test_handle_text_file_saved(self):

        """Asserts text file is exists (after being converted and saved in handle_converting_pdf_to_text"""

        self.assertEqual(os.path.exists(os.path.join(settings.MEDIA_ROOT, "converted_text.txt")), True)

    def test_check_txt_file_starts_with_specific_string(self):

        """Asserts text file starts with specified string from PDF file"""

        with open(os.path.join(settings.MEDIA_ROOT, "converted_text.txt")) as f:
            content = f.read()
            self.assertTrue(content.startswith("RE"))

    def test_check_txt_file_ends_with_specific_string(self):

        """Asserts text file ends with specified string from PDF file"""

        with open(os.path.join(settings.MEDIA_ROOT, "converted_text.txt")) as f:
            content = f.read()
            content = content.strip("\n")
            self.assertTrue(content.endswith("discharge."))

    def test_pdf_view_returns_http_response(self):

        """Asserts that the response of the HTTPResponse is 200"""

        file_path = os.path.join(settings.MEDIA_ROOT, "converted_text.txt")
        with open(file_path, 'r') as f:
            # Set the content type
            response = HttpResponse(f.read(), content_type='text/plain')
            # Set the attachment and filename
            response['Content-Disposition'] = 'attachment; filename=' + '"' + os.path.basename(file_path)
            self.assertEqual(response.status_code, 200)


class TxtConverterTest(RouteTemplateTester):

    def setUp(self):

        """Opens Static txt file for testing and uses the client to post form data"""

        with open(TXT_FILE, 'rb') as f:
            upload_file = f.read()
            self.form_data = {'file': SimpleUploadedFile(f.name, upload_file)}
            self.response = self.client.post(reverse('txt'), self.form_data)

    def tearDown(self):

        """Removes all files in MEDIA_ROOT directory once test is completed"""

        [os.remove(os.path.join(settings.MEDIA_ROOT, x)) for x in os.listdir(settings.MEDIA_ROOT)]

    def test_txt_converter_page_returns_template(self):

        """Assert template is used"""

        self.route(reverse('txt'), 'txt.html')

    def test_can_save_data_from_POST_request(self):

        """Assert object has been saved"""

        self.assertEqual(PatientData.objects.count(), 1)
        new_patient_data = PatientData.objects.first()
        self.assertEqual(new_patient_data.mr_num, 240804)
