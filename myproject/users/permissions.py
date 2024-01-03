from rest_framework import permissions

class IsProviderUser(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return request.user.type == "P"
        except AttributeError:
            return {"error":"not autorization"}

class IsConsumerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return request.user.type == "C"
        except AttributeError:
            return {"error": "not autorization"}
