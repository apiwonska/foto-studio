from django.test import Client, TestCase
from django.urls import resolve, reverse

from .views import HomePageView


class UrlsTest(TestCase):

    def test_home_url_resolves(self):
        self.assertEqual(
            resolve(reverse('home')).func.view_class, HomePageView)


class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_view_status_code_ok(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_use_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'core/base.html', 'core/home.html')
