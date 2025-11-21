from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_mail_about_delete(title: str, user_email: str) -> str:
    send_mail(
        'Удаление урока',
        f'Урок "{title}" был удалён',
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )

    return f'Email about deletion lesson "{title}" for {user_email} sent successfully'
