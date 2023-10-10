from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Course(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.title


class CourseAccess(models.Model):
    user = models.ForeignKey(User, models.PROTECT)
    course = models.ForeignKey(Course, models.PROTECT, 'accesses')
    is_valid = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f'{self.user}-access-{self.course}'
