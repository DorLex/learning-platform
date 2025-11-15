from django.contrib.auth.models import User
from django.db.models import F, FilteredRelation, Q, QuerySet
from rest_framework.generics import get_object_or_404

from course_catalog.models import CourseAccess
from educational_content.models import Lesson


def _get_access_courses_by_user(user: User) -> QuerySet:
    return CourseAccess.objects.filter(user=user, is_valid=True)


def get_lessons_with_view_info(user: User) -> QuerySet:
    access_courses: QuerySet = _get_access_courses_by_user(user)

    lessons_with_view_info: QuerySet = (
        Lesson.objects.filter(courses__id__in=access_courses.values('course_id'))
        .values('title')
        .alias(
            view_info=FilteredRelation(
                'views',
                condition=Q(views__user=user),
            ),
        )
        .annotate(
            course=F('courses__title'),
            viewing_status=F('view_info__viewing_status'),
            viewing_time=F('view_info__viewing_time'),
        )
    )

    return lessons_with_view_info


def get_lessons_by_course(user: User, course_id: int) -> QuerySet:
    access_courses: QuerySet = _get_access_courses_by_user(user)

    access_course_id: int = get_object_or_404(
        access_courses.values_list('course_id', flat=True),
        course_id=course_id,
    )

    lessons_by_course: QuerySet = (
        Lesson.objects.filter(courses__id=access_course_id)
        .values('title')
        .alias(
            view_info=FilteredRelation(
                'views',
                condition=Q(views__user=user),
            ),
        )
        .annotate(
            viewing_status=F('view_info__viewing_status'),
            viewing_time=F('view_info__viewing_time'),
            last_viewing_time=F('view_info__last_viewing_time'),
        )
    )

    return lessons_by_course
