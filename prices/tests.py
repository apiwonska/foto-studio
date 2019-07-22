from django.test import Client, TestCase
from django.urls import resolve, reverse

from .factories import PriceFactory, PriceListFactory
from .views import PricesPageView


class UrlsTest(TestCase):

    def test_prices_url_resolves(self):
        self.assertEqual(resolve(reverse('prices:prices')
                                 ).func.view_class, PricesPageView)


class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_prices_view_response_status_ok(self):
        response = self.client.get(reverse('prices:prices'))
        self.assertEqual(response.status_code, 200)

    def test_prices_view_loads_correct_template(self):
        response = self.client.get(reverse('prices:prices'))
        self.assertTemplateUsed(
            response, 'core/base.html', 'prices/prices.html')

    def test_prices_view_loads_correct_context(self):
        price_list_objects = PriceListFactory.create_batch(3)
        for i in range(5):
            PriceFactory(price_list=price_list_objects[0])
        response = self.client.get(reverse('prices:prices'))
        self.assertEqual(len(response.context['price_lists']), 3)
        self.assertEqual(len(response.context['prices']), 5)


class PriceListModelTest(TestCase):

    def setUp(self):
        self.price_list = PriceListFactory()

    def test_title_is_required(self):
        self.assertFalse(self.price_list._meta.get_field(
                         'title_price_list').blank)
        self.assertFalse(self.price_list._meta.get_field(
                         'title_price_list').null)

    def test_order_is_required(self):
        self.assertFalse(self.price_list._meta.get_field('order').blank)
        self.assertFalse(self.price_list._meta.get_field('order').null)

    def test_object_name_is_correct(self):
        desired_object_name = str(
            self.price_list.order) + '. ' + self.price_list.title_price_list
        self.assertEqual(str(self.price_list), desired_object_name)


class PriceModelTest(TestCase):

    def setUp(self):
        self.price = PriceFactory()

    def test_price_list_is_required(self):
        self.assertFalse(self.price._meta.get_field('price_list').blank)
        self.assertFalse(self.price._meta.get_field('price_list').null)

    def test_service_is_required(self):
        self.assertFalse(self.price._meta.get_field('service').blank)
        self.assertFalse(self.price._meta.get_field('service').null)

    def test_price_is_required(self):
        self.assertFalse(self.price._meta.get_field('price').blank)
        self.assertFalse(self.price._meta.get_field('price').null)

    def test_order_is_required(self):
        self.assertFalse(self.price._meta.get_field('order').blank)
        self.assertFalse(self.price._meta.get_field('order').null)

    def test_object_name_is_correct(self):
        desired_object_name = (
            f'{self.price.price_list} - {self.price.order}.Cena: {self.price.service}')
        self.assertEqual(str(self.price), desired_object_name)
