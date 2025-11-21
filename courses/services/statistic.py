from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import Count, F, IntegerField, OuterRef, Q, QuerySet, Subquery, Sum

from courses.models import Course
from lessons.choices import ViewingStatusChoices

User: type[AbstractBaseUser] = get_user_model()


def _get_total_users_count() -> int:
    return User.objects.count()


def get_viewed_lessons_count_subquery() -> QuerySet:
    viewed_lessons_count_subquery: QuerySet = (
        Course.objects.annotate(
            viewed_lessons_count=Count(
                'lessons__views',
                filter=Q(lessons__views__viewing_status=ViewingStatusChoices.VIEWED),
            ),
        )
        .filter(pk=OuterRef('id'))
        .values('viewed_lessons_count')
    )

    return viewed_lessons_count_subquery


def get_total_view_time_subquery() -> QuerySet:
    total_view_time_subquery: QuerySet = (
        Course.objects.annotate(
            total_view_time=Sum('lessons__views__viewing_time'),
        )
        .filter(pk=OuterRef('id'))
        .values('total_view_time')
    )

    return total_view_time_subquery


def get_access_users_on_product_count_subquery() -> QuerySet:
    access_users_on_product_count_subquery: QuerySet = (
        Course.objects.annotate(
            access_users_on_product_count=Count(
                'accesses',
                filter=Q(accesses__is_valid=True),
            ),
        )
        .filter(pk=OuterRef('id'))
        .values('access_users_on_product_count')
    )

    return access_users_on_product_count_subquery


def get_course_statistics() -> QuerySet:
    total_users_count: int = _get_total_users_count()

    viewed_lessons_count_subquery: QuerySet = get_viewed_lessons_count_subquery()
    total_view_time_subquery: QuerySet = get_total_view_time_subquery()
    access_users_on_product_count_subquery: QuerySet = get_access_users_on_product_count_subquery()

    course_statistics: QuerySet = Course.objects.all().annotate(
        viewed_lessons_count=Subquery(
            viewed_lessons_count_subquery,
            output_field=IntegerField(),
        ),
        total_view_time=Subquery(
            total_view_time_subquery,
            output_field=IntegerField(),
        ),
        access_users_on_product_count=Subquery(
            access_users_on_product_count_subquery,
            output_field=IntegerField(),
        ),
        percent_users_buy=F('access_users_on_product_count') / float(total_users_count) * 100,
    )

    return course_statistics
