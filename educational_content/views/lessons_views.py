from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from educational_content.serializers import lessons_serializers
from educational_content.services.get_db import get_lessons_with_view_info, get_lessons_by_course


class LessonsAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset = get_lessons_with_view_info(request.user)
        serializer = lessons_serializers.LessonsWithInfoSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = lessons_serializers.LessonsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class LessonsByCourseAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, course_id):
        queryset = get_lessons_by_course(request.user, course_id)
        serializer = lessons_serializers.LessonsWithInfoByCourseSerializer(queryset, many=True)

        return Response(serializer.data)