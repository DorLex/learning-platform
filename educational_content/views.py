from django.db.models import FilteredRelation, Q, F
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from course_catalog.models import CourseAccess
from .models import Lesson
from .serializers import LessonsSerializer, LessonsByCourseSerializer


class LessonsViewSet(viewsets.ViewSet):

    def list(self, request):
        access_courses = CourseAccess.objects.filter(user=request.user, is_valid=True)

        queryset = (
            Lesson.objects
            .filter(courses__id__in=access_courses.values('course_id'))
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


class LessonsByCourseViewSet(viewsets.ViewSet):

    def list(self, request, course_id):
        access_courses = CourseAccess.objects.filter(user=request.user, is_valid=True)

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
                    condition=Q(views__user=request.user)
                )
            )

            .annotate(
                viewing_status=F('view_info__viewing_status'),
                viewing_time=F('view_info__viewing_time'),
                last_viewing_time=F('view_info__last_viewing_time'),
            )

        )

        serializer = LessonsByCourseSerializer(queryset, many=True)

        return Response(serializer.data)
