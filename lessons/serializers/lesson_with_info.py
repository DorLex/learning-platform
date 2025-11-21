from rest_framework import serializers

from lessons.models import Lesson


class LessonWithInfoSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField()
    viewing_status = serializers.CharField(allow_null=True)
    viewing_time = serializers.IntegerField(allow_null=True)

    class Meta:
        model: type[Lesson] = Lesson

        fields: tuple = (
            'course_title',
            'title',
            'viewing_status',
            'viewing_time',
        )
