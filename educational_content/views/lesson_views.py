from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from educational_content.models import Lesson
from educational_content.serializers import lessons_serializers


class LessonAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, lesson_id):
        obj = get_object_or_404(Lesson, pk=lesson_id)
        serializer = lessons_serializers.LessonsSerializer(obj)

        return Response(serializer.data)

    def put(self, request, lesson_id):
        obj = get_object_or_404(Lesson, pk=lesson_id)
        serializer = lessons_serializers.LessonsSerializer(obj, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def patch(self, request, lesson_id):
        obj = get_object_or_404(Lesson, pk=lesson_id)
        serializer = lessons_serializers.LessonsSerializer(obj, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # return Response(serializer.data)
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, lesson_id):
        obj = get_object_or_404(Lesson, pk=lesson_id)
        obj.delete()
        serializer = lessons_serializers.LessonsSerializer(obj)

        return Response(serializer.data, status.HTTP_204_NO_CONTENT)
