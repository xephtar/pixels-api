from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail


def index(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['omerfdavarci@gmail.com', ]
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse(status=200)
