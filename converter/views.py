from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from converter.forms import PdfConverterForm
from converter.handlers import handle_upload_file


# Create your views here.
def index(request):
    return render(request, 'home.html')


def converted_pdf(request):
    return HttpResponse('ok')


def pdf(request):
    form = PdfConverterForm()

    if request.method == 'POST':
        form = PdfConverterForm(request.POST, request.FILES)
        if form.is_valid():
            handle_upload_file(request.FILES['file'])
            return redirect('converted_pdf')

    return render(request, 'pdf.html', {'form': form})



