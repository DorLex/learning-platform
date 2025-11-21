from django.db.models import QuerySet
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework.views import APIView

from courses.permissions import IsAdminOrAuthRead
from lessons.serializers.lesson import LessonSerializer
from lessons.serializers.lesson_with_info import LessonWithInfoSerializer
from lessons.services.crud import get_lessons_with_view_info
from lessons.services.lesson import LessonService


@extend_schema(tags=['Lessons'])
class LessonsWithInfoAPIView(APIView):
    permission_classes: tuple = (IsAdminOrAuthRead,)

    @extend_schema(responses=LessonWithInfoSerializer(many=True))
    def get(self, request: Request) -> Response:
        lessons: QuerySet = get_lessons_with_view_info(request.user)
        serializer: LessonWithInfoSerializer = LessonWithInfoSerializer(lessons, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=LessonSerializer,
        responses={status.HTTP_201_CREATED: LessonSerializer},
    )
    def post(self, request: Request) -> Response[ReturnDict]:
        lesson_service: LessonService = LessonService()
        lesson: ReturnDict = lesson_service.create_lesson(request.data)
        return Response(lesson, status.HTTP_201_CREATED)
