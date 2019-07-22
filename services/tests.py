from django.test import Client, TestCase
from django.urls import resolve, reverse

from .models import FotoPortrait, FotoStudio, FotoWedding
from .views import (
    FotoPortraitListView,
    FotoWeddingListView,
    FotoStudioListView)


class UrlsTest(TestCase):

    def test_foto_portrait_url_resolves(self):
        self.assertEqual(
            resolve(reverse('services:foto_portrait')).func.view_class,
            FotoPortraitListView)

    def test_foto_weddings_url_resolves(self):
        self.assertEqual(
            resolve(reverse('services:foto_weddings')).func.view_class,
            FotoWeddingListView)

    def test_lease_url_resolves(self):
        self.assertEqual(
            resolve(reverse('services:lease')).func.view_class,
            FotoStudioListView)


class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_gallery_portrait_list_view_response_status_ok(self):
        response = self.client.get(reverse('services:foto_portrait'))
        self.assertEqual(response.status_code, 200)

    def test_gallery_weddings_list_view_response_status_ok(self):
        response = self.client.get(reverse('services:foto_weddings'))
        self.assertEqual(response.status_code, 200)

    def test_gallery_studio_list_view_response_status_ok(self):
        response = self.client.get(reverse('services:lease'))
        self.assertEqual(response.status_code, 200)


class FotoPortraitModelTest(TestCase):

    def setUp(self):
        self.foto_portrait = FotoPortrait.objects.create(order=1)

    def test_object_name_is_correct(self):
        desired_object_name = str(
            self.foto_portrait.order) + ". Fotografia Portretowa"
        self.assertEqual(str(self.foto_portrait), desired_object_name)


class FotoWeddingModelTest(TestCase):

    def setUp(self):
        self.foto_wedding = FotoWedding.objects.create(order=1)

    def test_object_name_is_correct(self):
        desired_object_name = str(
            self.foto_wedding.order) + ". Fotografia Weselna"
        self.assertEqual(str(self.foto_wedding), desired_object_name)


class FotoStudioModelTest(TestCase):

    def setUp(self):
        self.foto_studio = FotoStudio.objects.create(order=1)

    def test_object_name_is_correct(self):
        desired_object_name = str(self.foto_studio.order) + ". Studio"
        self.assertEqual(str(self.foto_studio), desired_object_name)
