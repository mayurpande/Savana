from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch, call

from functional_tests.test_pdf_to_text_converter_page import PDF_FILE
from converter.forms import PdfConverterForm


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

    def test_pdf_converter_page_returns_template(self):

        self.route(reverse('pdf'), 'pdf.html')

    @patch('converter.views.handle_upload_file')
    def test_POST_form_redirects(self, mock_handle_upload_file):
        with open(PDF_FILE, 'rb') as f:
            upload_file = f.read()
            post_dict = {'title': 'test title'}
            form_data = {'file': SimpleUploadedFile(f.name, upload_file)}
            response = self.client.post(reverse('pdf'), form_data)
            self.assertEqual(mock_handle_upload_file.called, True)
            self.assertRedirects(response, reverse('converted_pdf'))

    @patch('converter.views.handle_upload_file')
    def test_POST_form_saves_file_as_pdf(self, mock_handle_upload_file):
        with open(PDF_FILE, 'rb') as f:
            upload_file = f.read()
            post_dict = {'title': 'test title'}
            form_data = {'file': SimpleUploadedFile(f.name, upload_file)}
            self.client.post(reverse('pdf'), form_data)
            self.assertEqual(mock_handle_upload_file.called, True)


