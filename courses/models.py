from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

User: type[AbstractBaseUser] = get_user_model()


class Course(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    class Meta:
        verbose_name: str = 'Курс'
        verbose_name_plural: str = 'Курсы'

    def __str__(self) -> str:
        return f'[{self.pk}] {self.title}'


class CourseAccess(models.Model):
    user = models.ForeignKey(User, models.PROTECT)
    course = models.ForeignKey(Course, models.PROTECT, 'accesses')
    is_valid = models.BooleanField(default=True)

    class Meta:
        unique_together: tuple = ('user', 'course')
        verbose_name: str = 'Доступ к курсу'
        verbose_name_plural: str = 'Доступ к курсам'

    def __str__(self) -> str:
        return f'{self.user} <-access-> {self.course}'
