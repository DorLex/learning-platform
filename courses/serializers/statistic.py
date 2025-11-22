from rest_framework import serializers


class CourseStatisticSerializer(serializers.Serializer):
    title = serializers.CharField()
    viewed_lessons_count = serializers.IntegerField()
    view_time_sum = serializers.IntegerField()
    access_count = serializers.IntegerField()
    users_buy_percent = serializers.FloatField()
