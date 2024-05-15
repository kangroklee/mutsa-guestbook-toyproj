from rest_framework.permissions import BasePermission

class IsPostOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if 'passcode' not in request.data:
            return False
        return request.data['passcode'] == obj.passcode
