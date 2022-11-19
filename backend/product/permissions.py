from rest_framework import permissions


class IsReadOnlyButStaff(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH", "POST", "DELETE")

    def has_permission(self, request, view):
        if request.user.is_staff or request.method not in self.edit_methods:
            return True

        return False


class IsReadOnlyButUser(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH", "POST", "DELETE")

    def has_permission(self, request, view):
        if request.user.is_authenticated or request.method not in self.edit_methods:
            return True

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        else:
            return False

        return False
