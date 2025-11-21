from rest_framework.generics import get_object_or_404
from rest_framework.utils.serializer_helpers import ReturnDict

from lessons.models import Lesson
from lessons.serializers.lesson import LessonSerializer


class LessonService:
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
