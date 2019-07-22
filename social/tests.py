from django.test import RequestFactory, TestCase
from django.urls import reverse

from .models import Link
from .processors import ctx_dict


class LinkModelTest(TestCase):

    def setUp(self):
        self.link = Link.objects.create(
            key='test-key', name='test name', url='https://www.facebook.com/')

    def test_key_is_unique(self):
        self.assertTrue(self.link._meta.get_field('key').unique)

    def test_object_name_is_name(self):
        self.assertEqual(str(self.link), self.link.name)


class ProcessorsTest(TestCase):

    def test_ctx_dict_resturns_context(self):
        Link.objects.create(key='link1', name='link1', url='https://www.link1.com/')
        Link.objects.create(key='link2', name='link2', url='https://www.link2.com/')
        Link.objects.create(key='link3', name='link3', url='https://www.link3.com/')
        request = RequestFactory().get(reverse('home'))
        desired_result = {
            'link1': 'https://www.link1.com/',
            'link2': 'https://www.link2.com/',
            'link3': 'https://www.link3.com/'
        }
        self.assertEqual(ctx_dict(request), desired_result)
