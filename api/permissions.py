from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user and (request.user.is_staff or obj.created_by == request.user):
            return True
        return False

class IsAdminOrNGO(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user and (request.user.is_staff or obj.created_by == request.user):
            return True
        return False

class IsHealthVolunteer(permissions.BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user, 'is_healthworker',True)








