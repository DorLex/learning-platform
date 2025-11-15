from rest_framework import serializers

from educational_content.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields: str | tuple = '__all__'
