from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from courses.models import Course
from lessons.choices import ViewingStatusChoices

User: type[AbstractBaseUser] = get_user_model()


class Lesson(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    video_url = models.URLField(max_length=255)
    video_duration = models.PositiveSmallIntegerField(default=0)

    courses = models.ManyToManyField(Course, 'lessons', blank=True)

    class Meta:
        verbose_name: str = 'Урок'
        verbose_name_plural: str = 'Уроки'

    def __str__(self) -> str:
        return f'[{self.id}] {self.title}'


class LessonViewInfo(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    lesson = models.ForeignKey(Lesson, models.CASCADE, 'views')

    viewing_time = models.PositiveSmallIntegerField(default=0)
    last_viewing_time = models.DateTimeField(auto_now=True)
    viewing_status = models.CharField(
        max_length=10,
        choices=ViewingStatusChoices.choices,
        default=ViewingStatusChoices.not_viewed,
    )

    class Meta:
        unique_together: tuple = ('user', 'lesson')
        verbose_name: str = 'Инфо просмотров урока'
        verbose_name_plural: str = 'Инфо просмотров уроков'

    def __str__(self) -> str:
        return f'{self.user} <-view-> {self.lesson}'
