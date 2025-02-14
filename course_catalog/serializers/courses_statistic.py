from rest_framework import serializers


class CourseStatisticsSerializer(serializers.Serializer):
    title = serializers.CharField()
    viewed_lessons_count = serializers.IntegerField()
    total_view_time = serializers.IntegerField()
    access_users_on_product_count = serializers.IntegerField()
    percent_users_buy = serializers.FloatField()
