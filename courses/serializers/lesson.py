from rest_framework import serializers

from lessons.models import Lesson


class LessonWithInfoByCourseSerializer(serializers.ModelSerializer):
    viewing_status = serializers.CharField()
    viewing_time = serializers.IntegerField()
    last_viewing_time = serializers.DateTimeField()

    class Meta:
        model: type[Lesson] = Lesson

        fields: tuple = (
            'title',
            'viewing_status',
            'viewing_time',
            'last_viewing_time',
        )
