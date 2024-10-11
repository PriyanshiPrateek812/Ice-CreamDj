from django.core.mail import send_mail
from django.conf import settings

def send_mail_to_client():
    subject = 'Your order has been placed successfully'
    message = 'Thank you for your order. We will contact you soon'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['priyanshiprateek00@gmail.com']
    send_mail(subject, message, from_email, recipient_list)