from rest_framework.permissions import BasePermission

# here I can custom the user permissions by their roles
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "admin"
    
class IsManutentor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "manutentor"
    
class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "user"