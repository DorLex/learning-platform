import time

from celery import shared_task


@shared_task
def my_task():
    time.sleep(15)

    return '<return my_task>'
