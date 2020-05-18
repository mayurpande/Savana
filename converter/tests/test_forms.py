from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from converter.forms import PdfConverterForm


class PdfConverterFormTest(TestCase):

    def test_form_validation_for_blank_items(self):
        post_dict = {'title': ''}
        form_data = {'file': SimpleUploadedFile('file', '')}
        form = PdfConverterForm(post_dict, form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertIn('Title is required', form.errors['title'])
        print(form.errors)
        self.assertIn('file', form.errors.keys())
        self.assertIn('The submitted file is empty.', form.errors['file'])
