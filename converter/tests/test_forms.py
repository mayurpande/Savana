from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from converter.forms import PdfConverterForm, TxtJsonConverterForm
from functional_tests.test_pdf_to_text_converter_page import IMAGE_FILE, PDF_FILE
from functional_tests.test_txt_file_to_json_converter import TXT_FILE


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

    def test_form_is_true_if_pdf_file_is_submitted(self):
        with open(PDF_FILE, 'rb') as f:
            upload_file = f.read()
            post_dict = {'title': 'test title'}
            form_data = {'file': SimpleUploadedFile(f.name, upload_file)}
            form = PdfConverterForm(post_dict, form_data)
            self.assertTrue(form.is_valid())


class TxtJsonFormTest(TestCase):

    def test_form_is_false_if_empty(self):
        form_data = {'file': SimpleUploadedFile('file', '')}
        form = TxtJsonConverterForm('', form_data)
        self.assertFalse(form.is_valid())

    def test_form_is_false_if_non_txt_file_is_submitted(self):
        with open(IMAGE_FILE, 'rb') as f:
            upload_file = f.read()
            form_data = {'file': SimpleUploadedFile(f.name, upload_file)}
            form = TxtJsonConverterForm(f.name, form_data)
            self.assertFalse(form.is_valid())

    def test_form_is_true_if_txt_file_is_submitted(self):
        with open(TXT_FILE, 'rb') as f:
            upload_file = f.read()
            form_data = {'file': SimpleUploadedFile(f.name, upload_file)}
            form = TxtJsonConverterForm(f.name, form_data)
            self.assertTrue(form.is_valid())


