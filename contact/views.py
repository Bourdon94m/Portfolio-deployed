from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from contact.forms import ContactForm


def contact(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = form.cleaned_data['subject']

            if not name or not email or not message or not subject:
                messages.error(request, 'Champs manquant')
                return redirect('contact')
            else:
                # Envoi de l'e-mail
                send_mail(
                    subject,
                    message,
                    email,
                    ['matthieu.pro94@gmail.com'],  # Remplacez par l'adresse e-mail de destination
                    fail_silently=False,
                    # Mettez à True si vous ne voulez pas d'erreur affichée en cas d'échec de l'envoi
                )
                messages.success(request, 'Votre message a été envoyé avec succès !')
                return redirect('contact')  # Remplacez par le nom de votre vue de confirmation
    return render(request, 'contact/contact.html', {"form": form})
