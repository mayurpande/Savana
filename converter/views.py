import re
import uuid

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings

from converter.forms import PdfConverterForm, TxtJsonConverterForm
from converter.handlers import handle_upload_file, handle_converting_pdf_to_text

import os


# Create your views here.
from converter.models import PatientData


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
    form = TxtJsonConverterForm()

    if request.method == 'POST':
        form = TxtJsonConverterForm(request.POST, request.FILES)
        if form.is_valid():
            text_file = request.FILES['file']
            for chunk in text_file.chunks():
                str_text_file = chunk.decode('ascii')
                # Apply regex and get MR number group
                mr_num_reg = re.compile(r'MR: (\d+)')
                mo = mr_num_reg.search(str_text_file)
                if mo:
                    mr_num = int(mo.group(1))
                    # Get the index of the free text and slice string
                    ind_diagnosis = str_text_file.index('DIAGNOSES')
                    doc_text = str_text_file[ind_diagnosis:]
                    # Create a unique identifier for patient_id
                    patient_id = uuid.uuid4()
                    patient = PatientData(patient_id=patient_id, mr_num=mr_num, document_text=doc_text)
                    patient.save()
                    # Return json response
                    return JsonResponse({'patient_id': patient_id, 'document_text': doc_text})

    return render(request, 'txt.html', {'form': form})
