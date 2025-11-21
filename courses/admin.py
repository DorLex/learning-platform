from django.contrib import admin

from courses.models import Course, CourseAccess


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseAccess)
class CourseAccessAdmin(admin.ModelAdmin):
    pass
