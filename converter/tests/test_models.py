from django.test import TestCase

from converter.models import PatientData


class PatientModelTest(TestCase):

    def test_saving_and_retrieving_items(self):

        first_item = PatientData()
        first_item.mr_num = 28004
        first_item.patient_id = id(28004)
        first_item.document_text = "Some patient text"
        first_item.save()

        second_item = PatientData()
        second_item.mr_num = 28005
        second_item.patient_id = id(28005)
        second_item.document_text = "Some other patient text"
        second_item.save()

        saved_items = PatientData.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.patient_id, id(28004))
        self.assertEqual(second_saved_item.patient_id, id(28005))



