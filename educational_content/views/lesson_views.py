from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from educational_content.models import Lesson
from educational_content.serializers import lessons_serializers


class LessonAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, lesson_id):
        queryset = get_object_or_404(Lesson, pk=lesson_id)
        serializer = lessons_serializers.LessonsSerializer(queryset)

        return Response(serializer.data)
