from django.core import mail
from django.test import Client, TestCase
from django.urls import resolve, reverse

from .forms import ContactForm
from .views import contact


class UrlsTest(TestCase):

    def test_kontakt_url_resolves(self):
        self.assertEqual(resolve(reverse('contact:contact')).func, contact)


class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_view_contact_response_ok(self):
        response = self.client.get(reverse('contact:contact'))
        self.assertEqual(response.status_code, 200)

    def test_view_contact_uses_correct_template(self):
        response = self.client.get(reverse('contact:contact'))
        self.assertTemplateUsed(response, 'core/base.html', 'contact.html')

    def test_view_contact_contin_form_in_context(self):
        response = self.client.get(reverse('contact:contact'))
        self.assertTrue(response.context['form'])
        self.assertTrue(isinstance(response.context['form'], ContactForm))

    def test_view_contact_sends_message_if_the_form_is_valid(self):
        data = {'name': 'Paweł Kowalski', 'email': 'p.k@test.pl',
                'content': 'Lorem ipsum dolor sit amet.'}
        response = self.client.post(reverse('contact:contact'), data)
        self.assertRedirects(response, reverse(
            'contact:contact') + '?ok', status_code=302, target_status_code=200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject,
                         'Flesz FotoStudio: Nowa wiadomość')
        self.assertEqual(mail.outbox[0].body,
                         f"{data['name']} <{data['email']}> \n\n Napisał(a): \n\n {data['content']}")
        self.assertEqual(mail.outbox[0].reply_to, [data['email']])

    def test_view_contact_does_not_send_message_if_the_form_is_not_valid(self):
        data = {'name': '', 'email': 'p.k@test.pl',
                'content': 'Lorem ipsum dolor sit amet.'}
        response = self.client.post(reverse('contact:contact'), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 0)


class ContactFormTest(TestCase):

    def setUp(self):
        self.form = ContactForm()

    def test_name_is_required(self):
        self.assertTrue(self.form.fields['name'].required)

    def test_name_placeholder(self):
        self.assertEqual(self.form.fields['name'].widget.attrs[
                         'placeholder'], 'Wpisz Imię i Nazwisko')

    def test_email_is_required(self):
        self.assertTrue(self.form.fields['email'].required)

    def test_email_placeholder(self):
        self.assertEqual(self.form.fields['email'].widget.attrs[
                         'placeholder'], 'Wpisz email')

    def test_content_is_required(self):
        self.assertTrue(self.form.fields['content'].required)

    def test_content_placeholder(self):
        self.assertEqual(self.form.fields['content'].widget.attrs[
                         'placeholder'], 'Treść wiadomości')

    def test_form_is_valid(self):
        form = ContactForm({'name': 'Paweł Kowalski', 'email': 'p.k@test.pl',
                            'content': 'Lorem ipsum dolor sit amet.'})
        self.assertTrue(form.is_valid())

    def test_form_is_not_valid(self):
        form = ContactForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['To pole jest wymagane.'])
        self.assertEqual(form.errors['email'], ['To pole jest wymagane.'])
        self.assertEqual(form.errors['content'], ['To pole jest wymagane.'])
