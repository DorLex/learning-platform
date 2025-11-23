import logging
import os
from logging import INFO, Logger, getLogger

from celery import Celery

logging.basicConfig(level=INFO)
logger: Logger = getLogger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app: Celery = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Запуск:
# celery -A core worker -l info
