from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import Count, F, IntegerField, OuterRef, Q, QuerySet, Subquery, Sum
from rest_framework.utils.serializer_helpers import ReturnList

from courses.models import Course
from courses.serializers.statistic import CourseStatisticSerializer
from lessons.choices import ViewingStatusChoices

User: type[AbstractBaseUser] = get_user_model()


class StatisticService:
    def get_course_statistic(self) -> ReturnList:
        total_users_count: int = self._get_total_users_count()

        viewed_lessons_count_subquery: QuerySet[Course, dict] = self._get_viewed_lessons_count_subquery()
        view_time_sum_subquery: QuerySet[Course, dict] = self._get_view_time_sum_subquery()
        access_count_subquery: QuerySet[Course, dict] = self._get_access_count_subquery()

        courses_statistic: QuerySet[Course] = Course.objects.all().annotate(
            viewed_lessons_count=Subquery(
                viewed_lessons_count_subquery,
                output_field=IntegerField(),
            ),
            view_time_sum=Subquery(
                view_time_sum_subquery,
                output_field=IntegerField(),
            ),
            access_count=Subquery(
                access_count_subquery,
                output_field=IntegerField(),
            ),
            users_buy_percent=F('access_count') / float(total_users_count) * 100,
        )

        serializer: CourseStatisticSerializer = CourseStatisticSerializer(courses_statistic, many=True)
        return serializer.data

    def _get_viewed_lessons_count_subquery(self) -> QuerySet[Course, dict]:
        viewed_lessons_count_subquery: QuerySet[Course, dict] = (
            Course.objects.filter(
                pk=OuterRef('id'),
            )
            .annotate(
                viewed_lessons_count=Count(
                    'lessons__views',
                    filter=Q(lessons__views__viewing_status=ViewingStatusChoices.viewed),
                ),
            )
            .values('viewed_lessons_count')
        )

        return viewed_lessons_count_subquery

    def _get_view_time_sum_subquery(self) -> QuerySet[Course, dict]:
        view_time_sum_subquery: QuerySet[Course, dict] = (
            Course.objects.filter(
                pk=OuterRef('id'),
            )
            .annotate(
                view_time_sum=Sum('lessons__views__viewing_time'),
            )
            .values('view_time_sum')
        )

        return view_time_sum_subquery

    def _get_access_count_subquery(self) -> QuerySet[Course, dict]:
        access_count_subquery: QuerySet[Course, dict] = (
            Course.objects.filter(
                pk=OuterRef('id'),
            )
            .annotate(
                access_count=Count(
                    'accesses',
                    filter=Q(accesses__is_valid=True),
                ),
            )
            .values('access_count')
        )

        return access_count_subquery

    def _get_total_users_count(self) -> int:
        return User.objects.count()
