from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
from rest_framework.views import APIView

from courses.permissions import IsAdminOrAuthRead
from lessons.serializers.lesson import LessonSerializer
from lessons.serializers.lesson_with_info import LessonWithInfoSerializer
from lessons.services.lesson import LessonService


@extend_schema(tags=['Lessons'])
class LessonsAPIView(APIView):
    permission_classes: tuple = (IsAdminOrAuthRead,)

    @extend_schema(responses=LessonWithInfoSerializer(many=True))
    def get(self, request: Request) -> Response[ReturnList]:
        """Список уроков, доступных пользователю, с информацией о просмотрах"""

        lesson_service: LessonService = LessonService()
        lessons: ReturnList = lesson_service.get_lessons_with_view_info_by_user(request.user)
        return Response(lessons)

    @extend_schema(
        request=LessonSerializer,
        responses={status.HTTP_201_CREATED: LessonSerializer},
    )
    def post(self, request: Request) -> Response[ReturnDict]:
        lesson_service: LessonService = LessonService()
        lesson: ReturnDict = lesson_service.create_lesson(request.data)
        return Response(lesson, status.HTTP_201_CREATED)
