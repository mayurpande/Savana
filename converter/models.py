from django.db import models


# Create your models here.
class PatientData(models.Model):
    patient_id = models.IntegerField()
    mr_num = models.IntegerField()
    document_text = models.TextField(default='')

