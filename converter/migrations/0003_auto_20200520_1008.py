# Generated by Django 3.0.6 on 2020-05-20 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0002_auto_20200520_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdata',
            name='document_text',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='mr_num',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='patient_id',
            field=models.IntegerField(),
        ),
    ]
