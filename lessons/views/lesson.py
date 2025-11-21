from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from courses.permissions import IsAdminOrAuthRead
from lessons.models import Lesson
from lessons.serializers.lesson import LessonSerializer
from lessons.tasks import send_mail_about_delete


@extend_schema(tags=['Lessons'])
class LessonAPIView(APIView):
    permission_classes = (IsAdminOrAuthRead,)

    def get(self, _request: Request, lesson_id: int) -> Response:
        lesson: Lesson = get_object_or_404(Lesson, pk=lesson_id)
        serializer: LessonSerializer = LessonSerializer(lesson)

        return Response(serializer.data)

    def put(self, request: Request, lesson_id: int) -> Response:
        lesson: Lesson = get_object_or_404(Lesson, pk=lesson_id)
        serializer: LessonSerializer = LessonSerializer(lesson, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def patch(self, request: Request, lesson_id: int) -> Response:
        lesson: Lesson = get_object_or_404(Lesson, pk=lesson_id)
        serializer: LessonSerializer = LessonSerializer(lesson, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request: Request, lesson_id: int) -> Response:
        lesson: Lesson = get_object_or_404(Lesson, pk=lesson_id)
        lesson.delete()

        send_mail_about_delete.delay(lesson.title, request.user.email)

        serializer: LessonSerializer = LessonSerializer(lesson)

        return Response(serializer.data, status.HTTP_204_NO_CONTENT)
