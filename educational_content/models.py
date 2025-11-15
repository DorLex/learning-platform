from django.contrib.auth import get_user_model
from django.contrib.auth.models import User as DefaultUser
from django.db import models

from course_catalog.models import Course
from educational_content.choices import ViewingStatusChoices

User: DefaultUser = get_user_model()


class Lesson(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    video_url = models.URLField(max_length=255)
    video_duration = models.PositiveSmallIntegerField(default=0)

    courses = models.ManyToManyField(Course, 'lessons', blank=True)

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
        default=ViewingStatusChoices.NOT_VIEWED,
    )

    class Meta:
        unique_together = ('user', 'lesson')

    def __str__(self) -> str:
        return f'{self.user} <-view-> {self.lesson}'
