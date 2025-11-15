from rest_framework import serializers

from course_catalog.models import CourseAccess


class CourseAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseAccess
        fields: str | tuple = '__all__'
