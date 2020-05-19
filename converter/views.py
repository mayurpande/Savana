from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

from converter.forms import PdfConverterForm
from converter.handlers import handle_upload_file, handle_converting_pdf_to_text

import os


# Create your views here.
def index(request):
    return render(request, 'home.html')


def pdf(request):

    form = PdfConverterForm()

    if request.method == 'POST':
        form = PdfConverterForm(request.POST, request.FILES)
        if form.is_valid():
            # Save file to disk
            handle_upload_file(request.FILES['file'])
            # Convert saved pdf file to text file and save to disk
            handle_converting_pdf_to_text(request.FILES['file'])
            # Return response downloaded file
            file_path = os.path.join(settings.MEDIA_ROOT, "converted_text.txt")
            with open(file_path, 'r') as f:
                response = HttpResponse(f.read(), content_type='text/plain')
                response['Content-Disposition'] = 'attachment; filename=' + '"' + os.path.basename(file_path)
                return response

    return render(request, 'pdf.html', {'form': form})


def txt(request):

    return render(request, 'txt.html')
