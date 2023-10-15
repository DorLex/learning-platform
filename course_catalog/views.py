from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CoursesStatisticSerializer
from .services.get_db import get_courses


class CoursesStatisticAPIView(APIView):

    def get(self, request):
        queryset = get_courses()
        serializer = CoursesStatisticSerializer(queryset, many=True)

        return Response(serializer.data)
