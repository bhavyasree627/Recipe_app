from vege.models import Receipe
from django.core.mail import send_mail
from django.conf import settings

def send_email_to_client():
    subject="Regarding the Receipes app by Bhavya"
    message = "Hello, Your receipe has been added to our database. Please check it out"
    from_email=settings.EMAIL_HOST_USER
    receipient_list=['saivyjayanthisai0002@gmail.com']
    send_mail(subject,message,from_email,receipient_list)