from django.test import TestCase, Client
from django.urls import reverse
from .models import CategoryComplaint, Complaint

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = CategoryComplaint.objects.create(cat_name='Test Category', slug='test-category')

    def test_newItemForm_get(self):
        response = self.client.get(reverse('core:new'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newissue.html')

    def test_newItemForm_post_valid(self):
        data = {
            'name': 'Test Complaint',
            'description': 'This is a test complaint description.',
            'category': self.category.id,
            'hostel': 'old boys hostel',
            'block': 'enoch'
        }
        response = self.client.post(reverse('core:new'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Complaint.objects.filter(name='Test Complaint').exists())

    def test_newItemForm_post_invalid(self):
        data = {
            'name': '',  # Invalid as name is required
            'description': 'Test description'
        }
        response = self.client.post(reverse('core:new'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Complaint.objects.filter(description='Test description').exists())
        # Use context to access the form object
        form = response.context['form']
        self.assertIn('name', form.errors)
        self.assertEqual(form.errors['name'], ['This field is required.'])
