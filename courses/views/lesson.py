from django.db.models import QuerySet
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework.views import APIView

from courses.serializers.lesson import LessonWithInfoByCourseSerializer
from lessons.services.crud import get_lessons_by_course


@extend_schema(tags=['Courses'])
class LessonsByCourseAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(responses=LessonWithInfoByCourseSerializer(many=True))
    def get(self, request: Request, course_id: int) -> Response[ReturnList]:
        lessons: QuerySet = get_lessons_by_course(request.user, course_id)
        serializer: LessonWithInfoByCourseSerializer = LessonWithInfoByCourseSerializer(lessons, many=True)

        return Response(serializer.data)
