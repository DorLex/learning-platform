from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from course_catalog.permissions import IsAdminOrAuthRead
from educational_content.models import Lesson
from educational_content.serializers.lessons import LessonSerializer
from educational_content.tasks import send_mail_about_delete


class LessonAPIView(APIView):
    permission_classes = (IsAdminOrAuthRead,)

    def get(self, request: Request, lesson_id: int) -> Response:
        lesson: Lesson = get_object_or_404(Lesson, pk=lesson_id)
        serializer = LessonSerializer(lesson)

        return Response(serializer.data)

    def put(self, request: Request, lesson_id: int) -> Response:
        lesson: Lesson = get_object_or_404(Lesson, pk=lesson_id)
        serializer = LessonSerializer(lesson, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def patch(self, request: Request, lesson_id: int) -> Response:
        lesson: Lesson = get_object_or_404(Lesson, pk=lesson_id)
        serializer = LessonSerializer(lesson, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request: Request, lesson_id: int) -> Response:
        lesson: Lesson = get_object_or_404(Lesson, pk=lesson_id)
        lesson.delete()

        send_mail_about_delete.delay(lesson.title, request.user.email)

        serializer = LessonSerializer(lesson)

        return Response(serializer.data, status.HTTP_204_NO_CONTENT)
