from django.contrib.auth import get_user_model
from django.db.models import Count, F, Sum, Q, Subquery, OuterRef, IntegerField
from rest_framework import viewsets
from rest_framework.response import Response

from educational_content.choices import ViewingStatusChoices

from .models import Course
from .serializers import CoursesStatisticSerializer

User = get_user_model()


class CoursesStatistic(viewsets.ViewSet):
    def list(self, request):
        total_users_count = User.objects.count()

        viewed_lessons_count = (
            Course.objects.annotate(
                viewed_lessons_count=Count(
                    'lessons__views',
                    filter=Q(lessons__views__viewing_status=ViewingStatusChoices.VIEWED)
                )
            )
            .filter(pk=OuterRef('id'))
        )

        total_view_time = (
            Course.objects.annotate(
                total_view_time=Sum('lessons__views__viewing_time')
            )
            .filter(pk=OuterRef('id'))
        )

        access_users_on_product_count = (
            Course.objects.annotate(
                access_users_on_product_count=Count(
                    'accesses',
                    filter=Q(accesses__is_valid=True),
                )
            )
            .filter(pk=OuterRef('id'))
        )

        queryset = (
            Course.objects.all()
            .annotate(
                viewed_lessons_count=Subquery(
                    viewed_lessons_count.values('viewed_lessons_count'),
                    output_field=IntegerField()
                ),

                total_view_time=Subquery(
                    total_view_time.values('total_view_time'),
                    output_field=IntegerField()
                ),

                access_users_on_product_count=Subquery(
                    access_users_on_product_count.values('access_users_on_product_count'),
                    output_field=IntegerField()
                ),

                percent_users_buy=F('access_users_on_product_count') / float(total_users_count) * 100
            )
        )

        # queryset = (
        #     Course.objects.all()
        #
        #     .annotate(
        #         viewed_lessons_count=Count(
        #             'lessons__views',
        #             filter=Q(lessons__views__viewing_status=ViewingStatusChoices.VIEWED),
        #             distinct=True
        #         ),
        #
        #         total_view_time=Sum('lessons__views__viewing_time'),
        #
        #         access_users_on_product_count=Count(
        #             'accesses',
        #             filter=Q(accesses__is_valid=True),
        #             distinct=True
        #         ),
        #
        #         percent_users_buy=F('access_users_on_product_count') / float(total_users_count) * 100
        #     )
        # )

        serializer = CoursesStatisticSerializer(queryset, many=True)

        return Response(serializer.data)
