import os

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from functional_tests.test_pdf_to_text_converter_page import PDF_FILE


# Create your tests here.
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

    def test_POST_form_redirects(self):

        """Asserts redirect"""

        self.assertRedirects(self.response, reverse('converted_pdf'))

    def test_POST_form_saves_file_as_pdf(self):

        """Asserts pdf file is exists (after being saved from handle_upload_file)"""

        self.assertEqual(os.path.exists(os.path.join(settings.MEDIA_ROOT, "Report1.pdf")), True)

    def test_handle_convert_pdf_to_text(self):

        """Asserts text file is exists (after being converted and saved in handle_converting_pdf_to_text"""

        self.assertEqual(os.path.exists(os.path.join(settings.MEDIA_ROOT, "converted_text.txt")), True)







