from django.shortcuts import render
from django.contrib import messages


# Create your views here.
from converter.forms import PdfConverterForm


def index(request):

    return render(request, 'home.html')


def pdf(request):
    form = PdfConverterForm()

    return render(request, 'pdf.html', {'form': form})
