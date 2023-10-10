from django.contrib import admin

from course_catalog.models import Course, CourseAccess


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseAccess)
class CourseAccessAdmin(admin.ModelAdmin):
    pass
