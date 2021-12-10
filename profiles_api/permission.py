from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow User to edit their own profiles"""

    def has_object_permission(self, request, view, obj):
        """Check User is trying to update their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
