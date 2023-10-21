from rest_framework import serializers

from course_catalog.models import Course
from educational_content.models import Lesson


class LessonsSerializer(serializers.ModelSerializer):
    courses = serializers.SlugRelatedField(slug_field='title', many=True, queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonsWithInfoSerializer(serializers.ModelSerializer):
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


class LessonsWithInfoByCourseSerializer(serializers.ModelSerializer):
    viewing_status = serializers.CharField()
    viewing_time = serializers.IntegerField()
    last_viewing_time = serializers.DateTimeField()

    class Meta:
        model = Lesson

        fields = (
            'title',
            'viewing_status',
            'viewing_time',
            'last_viewing_time',
        )
