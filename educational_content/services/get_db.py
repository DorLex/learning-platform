from django.db.models import FilteredRelation, F, Q
from rest_framework.generics import get_object_or_404

from course_catalog.models import CourseAccess
from educational_content.models import Lesson


def get_access_courses(user):
    access_courses = CourseAccess.objects.filter(user=user, is_valid=True)

    return access_courses


def get_lessons(user):
    access_courses = get_access_courses(user)

    queryset = (
        Lesson.objects
        .filter(courses__id__in=access_courses.values('course_id'))
        .values('title')

        .alias(
            view_info=FilteredRelation(
                'views',
                condition=Q(views__user=user)
            )
        )

        .annotate(
            course=F('courses__title'),
            viewing_status=F('view_info__viewing_status'),
            viewing_time=F('view_info__viewing_time'),
        )
    )

    return queryset


def get_lessons_by_course(user, course_id):
    access_courses = get_access_courses(user)

    access_course_id = get_object_or_404(
        access_courses.values_list('course_id', flat=True),
        course_id=course_id
    )

    queryset = (
        Lesson.objects
        .filter(courses__id=access_course_id)
        .values('title')

        .alias(
            view_info=FilteredRelation(
                'views',
                condition=Q(views__user=user)
            )
        )

        .annotate(
            viewing_status=F('view_info__viewing_status'),
            viewing_time=F('view_info__viewing_time'),
            last_viewing_time=F('view_info__last_viewing_time'),
        )

    )

    return queryset
