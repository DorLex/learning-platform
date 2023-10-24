from course_catalog.models import CourseAccess


def get_courses_accesses():
    queryset = CourseAccess.objects.all()
    return queryset
