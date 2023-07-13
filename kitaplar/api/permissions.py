from rest_framework import permissions

class isAdminorReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin

class isUserorReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_permission(self, request, view):
        is_user = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_user


class isYorumSahibiOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user == obj.yorum_sahibi:
            return True
        else:
            return False