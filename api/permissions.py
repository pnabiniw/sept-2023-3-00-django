from rest_framework.permissions import BasePermission


class IsSuperAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_superuser)
