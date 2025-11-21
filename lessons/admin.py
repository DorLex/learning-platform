from django.contrib import admin

from lessons.models import Lesson, LessonViewInfo


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    filter_horizontal = ('courses',)


@admin.register(LessonViewInfo)
class LessonViewInfoAdmin(admin.ModelAdmin):
    pass
