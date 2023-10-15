from django.contrib.auth import get_user_model
from django.db.models import Count, Q, OuterRef, Sum, Subquery, F, IntegerField

from course_catalog.models import Course
from educational_content.choices import ViewingStatusChoices

User = get_user_model()


def get_total_users_count():
    total_users_count = User.objects.count()
    return total_users_count


def get_viewed_lessons_count_for_subquery():
    viewed_lessons_count_for_subquery = (
        Course.objects.annotate(
            viewed_lessons_count=Count(
                'lessons__views',
                filter=Q(lessons__views__viewing_status=ViewingStatusChoices.VIEWED)
            )
        )
        .filter(pk=OuterRef('id'))
        .values('viewed_lessons_count')
    )

    return viewed_lessons_count_for_subquery


def get_total_view_time_for_subquery():
    total_view_time_for_subquery = (
        Course.objects.annotate(
            total_view_time=Sum('lessons__views__viewing_time')
        )
        .filter(pk=OuterRef('id'))
        .values('total_view_time')
    )

    return total_view_time_for_subquery


def get_access_users_on_product_count_for_subquery():
    access_users_on_product_count_for_subquery = (
        Course.objects.annotate(
            access_users_on_product_count=Count(
                'accesses',
                filter=Q(accesses__is_valid=True),
            )
        )
        .filter(pk=OuterRef('id'))
        .values('access_users_on_product_count')
    )

    return access_users_on_product_count_for_subquery


def get_courses():
    total_users_count = get_total_users_count()

    viewed_lessons_count_for_subquery = get_viewed_lessons_count_for_subquery()

    total_view_time_for_subquery = get_total_view_time_for_subquery()

    access_users_on_product_count_for_subquery = get_access_users_on_product_count_for_subquery()

    queryset = (
        Course.objects.all()
        .annotate(
            viewed_lessons_count=Subquery(
                viewed_lessons_count_for_subquery,
                output_field=IntegerField()
            ),

            total_view_time=Subquery(
                total_view_time_for_subquery,
                output_field=IntegerField()
            ),

            access_users_on_product_count=Subquery(
                access_users_on_product_count_for_subquery,
                output_field=IntegerField()
            ),

            percent_users_buy=F('access_users_on_product_count') / float(total_users_count) * 100
        )
    )

    return queryset
