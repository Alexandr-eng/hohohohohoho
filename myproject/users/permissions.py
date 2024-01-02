from rest_framework import permissions

class IsProviderUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.type == "P"

class IsConsumerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.type == "C"