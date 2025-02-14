from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_mail_about_delete(title, user_email):
    send_mail(
        'Удаление урока',
        f'Урок "{title}" был удалён',
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )

    return f'mail delete lesson "{title}" for {user_email} success'
