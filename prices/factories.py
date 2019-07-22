import factory

from .models import Price, PriceList


class PriceListFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = PriceList

    title_price_list = factory.Sequence(lambda n: f'price list {n}')
    order = 1


class PriceFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Price

    price_list = factory.SubFactory(PriceListFactory)
    service = factory.Sequence(lambda n: f'service name {n}')
    service_details = 'Lorem ipsum dolor sit amet.'
    price = 'starts from 1000'
    order = 1
