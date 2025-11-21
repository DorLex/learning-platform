from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework.views import APIView

from courses.permissions import IsAdminOrAuthRead
from lessons.models import Lesson
from lessons.serializers.lesson import LessonSerializer
from lessons.services.lesson import LessonService
from lessons.tasks import send_mail_about_delete


@extend_schema(tags=['Lessons'])
class LessonAPIView(APIView):
    permission_classes: tuple = (IsAdminOrAuthRead,)

    @extend_schema(responses=LessonSerializer)
    def get(self, _request: Request, lesson_id: int) -> Response[ReturnDict]:
        lesson_service: LessonService = LessonService()
        lesson: ReturnDict = lesson_service.get_lesson(lesson_id)
        return Response(lesson)

    @extend_schema(
        request=LessonSerializer,
        responses=LessonSerializer,
    )
    def put(self, request: Request, lesson_id: int) -> Response[ReturnDict]:
        lesson_service: LessonService = LessonService()
        lesson: ReturnDict = lesson_service.update_lesson(lesson_id, request.data)
        return Response(lesson)

    @extend_schema(
        request=LessonSerializer,
        responses=LessonSerializer,
    )
    def patch(self, request: Request, lesson_id: int) -> Response[ReturnDict]:
        lesson_service: LessonService = LessonService()
        lesson: ReturnDict = lesson_service.update_lesson(lesson_id, request.data, partial=True)
        return Response(lesson)

    def delete(self, request: Request, lesson_id: int) -> Response[ReturnDict]:
        lesson: Lesson = get_object_or_404(Lesson, pk=lesson_id)
        lesson.delete()

        send_mail_about_delete.delay(lesson.title, request.user.email)

        serializer: LessonSerializer = LessonSerializer(lesson)

        return Response(serializer.data, status.HTTP_200_OK)
