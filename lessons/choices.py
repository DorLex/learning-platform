from django.db import models


class ViewingStatusChoices(models.TextChoices):
    viewed = 'viewed', 'Просмотрено'
    not_viewed = 'not_viewed', 'Не просмотрено'
