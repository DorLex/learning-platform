import time

from celery import shared_task


@shared_task
def my_task():
    time.sleep(5)

    return '<return my_task>'
