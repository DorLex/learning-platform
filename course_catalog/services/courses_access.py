from django.db.models import QuerySet

from course_catalog.models import CourseAccess


def get_courses_accesses() -> QuerySet:
    return CourseAccess.objects.all()
