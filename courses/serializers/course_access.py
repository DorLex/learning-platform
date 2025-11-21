from rest_framework import serializers

from courses.models import CourseAccess


class CourseAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model: type[CourseAccess] = CourseAccess
        fields: str | tuple = '__all__'
