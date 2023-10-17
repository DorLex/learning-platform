from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CoursesStatisticSerializer
from .services.get_db import get_courses_statistic


class CoursesStatisticAPIView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        queryset = get_courses_statistic()
        serializer = CoursesStatisticSerializer(queryset, many=True)

        return Response(serializer.data)
