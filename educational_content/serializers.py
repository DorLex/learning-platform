from rest_framework import serializers
from .models import Lesson


class LessonsSerializer(serializers.ModelSerializer):
    course = serializers.CharField()
    viewing_status = serializers.CharField()
    viewing_time = serializers.IntegerField()

    class Meta:
        model = Lesson

        fields = (
            'course',
            'title',
            'viewing_status',
            'viewing_time',
        )
