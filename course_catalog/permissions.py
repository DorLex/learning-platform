from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView


class IsAdminOrAuthRead(BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        if request.method in SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        else:
            return bool(request.user and request.user.is_staff)
