from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from converter.forms import PdfConverterForm
from functional_tests.test_pdf_to_text_converter_page import IMAGE_FILE, PDF_FILE


class PdfConverterFormTest(TestCase):

    def test_form_validation_for_blank_items(self):
        post_dict = {'title': ''}
        form_data = {'file': SimpleUploadedFile('file', '')}
        form = PdfConverterForm(post_dict, form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertIn('Title is required', form.errors['title'])
        self.assertIn('file', form.errors.keys())
        self.assertIn('The submitted file is empty.', form.errors['file'])

    def test_form_is_false_if_non_pdf_file_is_submitted(self):
        with open(IMAGE_FILE, 'rb') as f:
            upload_file = f.read()
            post_dict = {'title': 'test title'}
            form_data = {'file': SimpleUploadedFile(f.name, upload_file)}
            form = PdfConverterForm(post_dict, form_data)
            self.assertFalse(form.is_valid())
            # self.assertIn('file', form.errors.keys())
            # self.assertIn('Allowed extensions are: pdf', form.errors['file'])

    def test_form_is_true_if_pdf_file_is_submitted(self):
        with open(PDF_FILE, 'rb') as f:
            upload_file = f.read()
            post_dict = {'title': 'test title'}
            form_data = {'file': SimpleUploadedFile(f.name, upload_file)}
            form = PdfConverterForm(post_dict, form_data)
            self.assertTrue(form.is_valid())

