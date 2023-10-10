from django.db.models import FilteredRelation, Q, F
from rest_framework import viewsets
from rest_framework.response import Response

from course_catalog.models import CourseAccess
from .models import Lesson
from .serializers import LessonsSerializer


class LessonsViewSet(viewsets.ViewSet):

    def list(self, request):
        access_courses_id = CourseAccess.objects.filter(user=request.user, is_valid=True).values('course_id')

        queryset = (
            Lesson.objects
            .filter(courses__id__in=access_courses_id)
            .values('title')

            .alias(
                view_info=FilteredRelation(
                    'views',
                    condition=Q(views__user=request.user)
                )
            )

            .annotate(
                course=F('courses__title'),
                viewing_status=F('view_info__viewing_status'),
                viewing_time=F('view_info__viewing_time'),
            )
        )

        serializer = LessonsSerializer(queryset, many=True)

        return Response(serializer.data)
