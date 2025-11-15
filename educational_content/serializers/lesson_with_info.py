from rest_framework import serializers

from educational_content.models import Lesson


class LessonWithInfoSerializer(serializers.ModelSerializer):
    course = serializers.CharField()
    viewing_status = serializers.CharField()
    viewing_time = serializers.IntegerField()

    class Meta:
        model = Lesson

        fields: tuple = (
            'course',
            'title',
            'viewing_status',
            'viewing_time',
        )


class LessonsWithInfoByCourseSerializer(serializers.ModelSerializer):
    viewing_status = serializers.CharField()
    viewing_time = serializers.IntegerField()
    last_viewing_time = serializers.DateTimeField()

    class Meta:
        model = Lesson

        fields: tuple = (
            'title',
            'viewing_status',
            'viewing_time',
            'last_viewing_time',
        )
