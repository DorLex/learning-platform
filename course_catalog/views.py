from django.contrib.auth import get_user_model
from django.db.models import Count, F, Sum, Q
from rest_framework import viewsets
from rest_framework.response import Response

from educational_content.choices import ViewingStatusChoices

from .models import Course
from .serializers import CoursesStatisticSerializer

User = get_user_model()


class CoursesStatistic(viewsets.ViewSet):
    def list(self, request):
        total_users_count = User.objects.count()

        queryset = (
            Course.objects.all()

            .annotate(
                viewed_lessons_count=Count(
                    'lessons__views',
                    filter=Q(lessons__views__viewing_status=ViewingStatusChoices.VIEWED),
                    distinct=True
                ),

                total_view_time=Sum('lessons__views__viewing_time'),

                access_users_on_product_count=Count(
                    'accesses',
                    filter=Q(accesses__is_valid=True),
                    distinct=True
                ),

                percent_users_buy=F('access_users_on_product_count') / float(total_users_count) * 100
            )
        )

        serializer = CoursesStatisticSerializer(queryset, many=True)

        return Response(serializer.data)
