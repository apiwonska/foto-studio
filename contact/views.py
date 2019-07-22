from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContactForm


def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')
            # sending en email
            email = EmailMessage(
                "Flesz FotoStudio: Nowa wiadomość",
                f"{name} <{email}> \n\n Napisał(a): \n\n {content}",
                "no-contestar@inbox.mailtrap.io",
                ["test85474562@test.pl"],
                reply_to=[email]
            )

            try:
                email.send()
                # everything went well, redirect to ok
                return redirect(reverse('contact:contact') + "?ok")
            except:
                # something went wrong, redirect to Fail
                return redirect(reverse('contact:contact') + "?fail")

    return render(request, "contact/contact.html", {'form': contact_form})
