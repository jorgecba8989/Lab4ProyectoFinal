from rest_framework import permissions


class DefaultPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        allowed_methods = ['POST','GET','PUT','PATCH','DELETE']

        if not request.user.is_authenticated:
            return False

        if request.method in allowed_methods:
            return True

class PlayListPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        allowed_methods = ['POST','GET','PUT','PATCH','DELETE']

        if request.user.is_authenticated and request.method in allowed_methods:
            return True

        return False