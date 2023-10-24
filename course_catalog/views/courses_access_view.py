from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from course_catalog.serializers import course_access_serializers
from course_catalog.services.courses_access_service import get_courses_accesses


class CoursesAccessAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset = get_courses_accesses()
        serializer = course_access_serializers.CourseAccessSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = course_access_serializers.CourseAccessSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
