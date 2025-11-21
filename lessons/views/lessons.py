from django.db.models import QuerySet
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from courses.permissions import IsAdminOrAuthRead
from lessons.serializers.lesson import LessonSerializer
from lessons.serializers.lesson_with_info import LessonWithInfoSerializer
from lessons.services.crud import get_lessons_with_view_info


@extend_schema(tags=['Lessons'])
class LessonsWithInfoAPIView(APIView):
    permission_classes = (IsAdminOrAuthRead,)

    @extend_schema(responses=LessonWithInfoSerializer(many=True))
    def get(self, request: Request) -> Response:
        lessons: QuerySet = get_lessons_with_view_info(request.user)
        serializer: LessonWithInfoSerializer = LessonWithInfoSerializer(lessons, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer: LessonSerializer = LessonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
