from django.db.models import QuerySet
from rest_framework.utils.serializer_helpers import ReturnList

from course_catalog.models import CourseAccess
from course_catalog.serializers.course_access import CourseAccessSerializer


class CourseService:
    def get_courses_accesses(self) -> ReturnList:
        courses_accesses: QuerySet[CourseAccess] = CourseAccess.objects.all()
        serializer: CourseAccessSerializer = CourseAccessSerializer(courses_accesses, many=True)
        return serializer.data
