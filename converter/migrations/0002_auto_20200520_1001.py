# Generated by Django 3.0.6 on 2020-05-20 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdata',
            name='document_text',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='patientdata',
            name='mr_num',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='patientdata',
            name='patient_id',
            field=models.TextField(default=''),
        ),
    ]