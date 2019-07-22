from django.test import Client, TestCase
from django.urls import resolve, reverse

from .models import Staff
from .views import AboutListView


class UrlsTest(TestCase):

    def test_about_url_resolves_to_about_list_view(self):
        self.assertEqual(resolve(reverse('about:about')
                                 ).func.view_class, AboutListView)


class ViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_about_list_view_status_ok(self):
        response = self.client.get(reverse('about:about'))
        self.assertEqual(response.status_code, 200)


class StaffModelTest(TestCase):

    def test_name_is_required(self):
        self.assertFalse(Staff._meta.get_field('name').blank)
        self.assertFalse(Staff._meta.get_field('name').null)

    def test_job_title_is_required(self):
        self.assertFalse(Staff._meta.get_field('job_title').blank)
        self.assertFalse(Staff._meta.get_field('job_title').null)

    def test_description_is_required(self):
        self.assertFalse(Staff._meta.get_field('description').blank)
        self.assertFalse(Staff._meta.get_field('description').null)

    def test_image_is_required(self):
        self.assertFalse(Staff._meta.get_field('image').blank)
        self.assertFalse(Staff._meta.get_field('image').null)

    def test_str_method(self):
        staff = Staff.objects.create(name='Marta', order=1)
        self.assertEqual(str(staff), '1. Pracownicy: Marta')
