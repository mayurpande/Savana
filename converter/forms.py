from django import forms
from django.core.validators import FileExtensionValidator


class PdfConverterForm(forms.Form):

    """Form attributes for file"""

    title = forms.CharField(max_length=100, error_messages={'required': 'Title is required'})
    file = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])], error_messages={
        'required': 'File of type PDF is required', 'invalid': 'File of type PDF is required'})
