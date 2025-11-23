from django.contrib.auth.models import User
from django.db.models import F, FilteredRelation, Q, QuerySet
from rest_framework.generics import get_object_or_404
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList

from courses.models import CourseAccess
from courses.services.course import CourseService
from lessons.models import Lesson
from lessons.serializers.lesson import LessonSerializer
from lessons.serializers.lesson_with_info import LessonWithInfoSerializer
from lessons.tasks import send_mail_about_delete


class LessonService:
    def create_lesson(self, lesson_data: dict) -> ReturnDict:
        serializer: LessonSerializer = LessonSerializer(data=lesson_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data

    def get_lesson(self, lesson_id: int) -> ReturnDict:
        lesson: Lesson = get_object_or_404(Lesson, pk=lesson_id)
        serializer: LessonSerializer = LessonSerializer(lesson)
        return serializer.data

    def update_lesson(self, lesson_id: int, lesson_data: dict, *, partial: bool = False) -> ReturnDict:
        lesson: Lesson = get_object_or_404(Lesson, pk=lesson_id)
        serializer: LessonSerializer = LessonSerializer(lesson, lesson_data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data

    def delete_lesson(self, lesson_id: int, user: User) -> ReturnDict:
        lesson: Lesson = get_object_or_404(Lesson, pk=lesson_id)
        lesson.delete()

        send_mail_about_delete.delay(lesson.title, user.email)

        serializer: LessonSerializer = LessonSerializer(lesson)
        return serializer.data

    def get_lessons_with_view_info_by_user(self, user: User) -> ReturnList:
        course_service: CourseService = CourseService()
        course_accesses: QuerySet[CourseAccess] = course_service.get_course_accesses_by_user(user)

        lessons_with_view_info: QuerySet[Lesson, dict] = (
            Lesson.objects.filter(
                courses__id__in=course_accesses.values('course_id'),
            )
            .values('title')
            .alias(
                view_info=FilteredRelation(
                    'views',
                    condition=Q(views__user=user),
                ),
            )
            .annotate(
                course_title=F('courses__title'),
                viewing_status=F('view_info__viewing_status'),
                viewing_time=F('view_info__viewing_time'),
            )
        )

        serializer: LessonWithInfoSerializer = LessonWithInfoSerializer(lessons_with_view_info, many=True)
        return serializer.data
