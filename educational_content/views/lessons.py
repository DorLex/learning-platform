from django.db.models import QuerySet
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from course_catalog.permissions import IsAdminOrAuthRead
from educational_content.serializers.lesson import LessonSerializer
from educational_content.serializers.lesson_with_info import (
    LessonsWithInfoByCourseSerializer,
    LessonWithInfoSerializer,
)
from educational_content.services.crud import get_lessons_by_course, get_lessons_with_view_info


@extend_schema(tags=['Lessons'])
class LessonsWithInfoAPIView(APIView):
    permission_classes = (IsAdminOrAuthRead,)

    def get(self, request: Request) -> Response:
        lessons: QuerySet = get_lessons_with_view_info(request.user)
        serializer: LessonWithInfoSerializer = LessonWithInfoSerializer(lessons, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer: LessonSerializer = LessonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


@extend_schema(tags=['Lessons'])
class LessonsWithInfoByCourseAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request, course_id: int) -> Response:
        lessons: QuerySet = get_lessons_by_course(request.user, course_id)
        serializer: LessonsWithInfoByCourseSerializer = LessonsWithInfoByCourseSerializer(lessons, many=True)

        return Response(serializer.data)
