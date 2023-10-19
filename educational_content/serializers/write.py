from rest_framework import serializers

from educational_content.models import Lesson


class LessonsWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
