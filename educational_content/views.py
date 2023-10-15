from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LessonsSerializer, LessonsByCourseSerializer
from .services.get_db import get_lessons, get_lessons_by_course


class LessonsAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset = get_lessons(request.user)
        serializer = LessonsSerializer(queryset, many=True)

        return Response(serializer.data)


class LessonsByCourseAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, course_id):
        queryset = get_lessons_by_course(request.user, course_id)
        serializer = LessonsByCourseSerializer(queryset, many=True)

        return Response(serializer.data)
