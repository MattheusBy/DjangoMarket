from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string

from shop_server.celery import app



@app.task
def mass_send_mail():
    list_recipients = []
    for user in User.objects.all():
        list_recipients.append(user.email)
    msg_html = render_to_string('market/mass_mail.html')
    subject = "Маркет.бай"
    message = "Найдите все интересующие Вас товары"
    from_email = "marketstuffdjango@gmail.com"
    send_mail(subject,
              message,
              from_email,
              list_recipients,
              html_message=msg_html,
              fail_silently=False)
    return f"sending emails"
