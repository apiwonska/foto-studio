from django.test import Client, TestCase
from django.urls import resolve, reverse

from .factories import CategoryFactory, PostFactory
from .views import CategoryDetailView, NewsListView, PostDetailView


class UrlsTest(TestCase):

    def test_url_posts_resolves(self):
        self.assertEqual(resolve(reverse('news:posts')
                                 ).func.view_class, NewsListView)

    def test_url_post_resolves(self):
        self.post = PostFactory()
        self.assertEqual(resolve(reverse('news:post', args=[self.post.pk])
                                 ).func.view_class, PostDetailView)

    def test_url_category_resolves(self):
        self.category = CategoryFactory()
        self.assertEqual(resolve(reverse('news:category', args=[self.category.pk])
                                 ).func.view_class, CategoryDetailView)


class ViewsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category = CategoryFactory()
        cls.post = PostFactory()

    def setUp(self):
        self.client = Client()

    def test_news_list_view_status_ok(self):
        response = self.client.get(reverse('news:posts'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view_status_ok(self):
        response = self.client.get(reverse('news:post', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_view_status_ok(self):
        response = self.client.get(
            reverse('news:category', args=[self.category.pk]))
        self.assertEqual(response.status_code, 200)


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(self):
        self.category = CategoryFactory()

    def test_name_is_required(self):
        self.assertFalse(self.category._meta.get_field('name').blank)
        self.assertFalse(self.category._meta.get_field('name').null)

    def test_object_name_is_name(self):
        self.assertEqual(str(self.category), self.category.name)


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(self):
        self.post = PostFactory()

    def test_title_is_required(self):
        self.assertFalse(self.post._meta.get_field('title').blank)
        self.assertFalse(self.post._meta.get_field('title').null)

    def test_content_is_required(self):
        self.assertFalse(self.post._meta.get_field('content').blank)
        self.assertFalse(self.post._meta.get_field('content').null)

    def test_object_name_is_title(self):
        self.assertEqual(str(self.post), self.post.title)
