from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
from services.models import Services
from blog.models import Post


def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def services(request):
    servicios = Services.objects.all()
    return render(request, 'core/services.html', {'servicios': servicios})


def store(request):
    return render(request, 'core/store.html')


def blog(request):
    posts = Post.objects.all()
    return render(request, 'core/blog.html', {'posts': posts})


def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Creamos el correo
            email_enviado = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                f"De {name} <{email}>\n\nEscribió:\n\n{content}",
                "no-contestar@inbox.mailtrap.io",
                ["jzambrano9974@utm.edu.ec"],
                reply_to=[email]
            )
            try:
                email_enviado.send()
                return redirect(reverse('contact') + "?ok")
            except:
                return redirect(reverse('contact') + "?fail")

    return render(request, 'core/contact.html', {'form': contact_form})