from django import forms
from django.core.validators import FileExtensionValidator


class PdfConverterForm(forms.Form):

    """Form attributes for file"""

    file = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'],
                                                              message='You are only allowed type of PDF.')])


class TxtJsonConverterForm(forms.Form):

    file = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['txt'],
                                                              message='You are only allowed type of TXT.')])
