from django.contrib.auth.models import User
import factory

from .models import Post, Category


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user {n}')


class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f'category {n}')


class PostFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Post

    title = factory.Sequence(lambda n: f'post {n}')
    content = 'Lorem ipsum dolor sit amet.'
    author = factory.SubFactory(UserFactory)
