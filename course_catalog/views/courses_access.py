from django.db.models import QuerySet
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from course_catalog.permissions import IsAdminOrAuthRead
from course_catalog.serializers.course_access import CourseAccessSerializer
from course_catalog.services.courses_access import get_courses_accesses


class CoursesAccessAPIView(APIView):
    permission_classes = (IsAdminOrAuthRead,)

    def get(self, request: Request) -> Response:
        access_to_courses: QuerySet = get_courses_accesses()
        serializer = CourseAccessSerializer(access_to_courses, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = CourseAccessSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
