from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from educational_content.models import Lesson
from course_catalog.permissions import IsAdminOrAuthRead
from educational_content.serializers import lesson_serializers


class LessonAPIView(APIView):
    permission_classes = (IsAdminOrAuthRead,)

    def get(self, request, lesson_id):
        obj = get_object_or_404(Lesson, pk=lesson_id)
        serializer = lesson_serializers.LessonSerializer(obj)

        return Response(serializer.data)

    def put(self, request, lesson_id):
        obj = get_object_or_404(Lesson, pk=lesson_id)
        serializer = lesson_serializers.LessonSerializer(obj, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def patch(self, request, lesson_id):
        obj = get_object_or_404(Lesson, pk=lesson_id)
        serializer = lesson_serializers.LessonSerializer(obj, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, lesson_id):
        obj = get_object_or_404(Lesson, pk=lesson_id)
        obj.delete()
        serializer = lesson_serializers.LessonSerializer(obj)

        return Response(serializer.data, status.HTTP_204_NO_CONTENT)
