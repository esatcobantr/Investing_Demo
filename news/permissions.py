from rest_framework.permissions import BasePermission


class IsSuperOrAuthorUser(BasePermission):
    message = "You are not an authorized user!"

    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user) or (request.user.is_superuser)


class IsSuperUser(BasePermission):
    message = "You are not an superuser!"

    def has_permission(self, request, view):
        return request.user.is_superuser
