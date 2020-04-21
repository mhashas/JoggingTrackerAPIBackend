from rest_framework.permissions import BasePermission


from api.models import AuthRole

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in self.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


class IsCreatingHasAccessOrNoAccess(BasePermission):
    """
    Either the user is trying to sign up, or no permissions
    """

    SAFE_METHODS = ['POST']

    def has_permission(self, request, view):
        if (request.method in self.SAFE_METHODS):
            return True

        if (request.user and request.user.is_authenticated):
            auth_role = AuthRole.objects.get(user_id__exact=request.user.pk) # type: AuthRole
            if auth_role.role == AuthRole.RoleTypes.ADMIN or auth_role.role == AuthRole.RoleTypes.MANAGER:
                return True

        return False

class HasAccessOrNoAccess(BasePermission):

    def has_permission(self, request, view):
        if (request.user and request.user.is_authenticated):
            auth_role = AuthRole.objects.get(user_id__exact=request.user.pk) # type: AuthRole
            if auth_role.role == AuthRole.RoleTypes.ADMIN or auth_role.role == AuthRole.RoleTypes.MANAGER:
                return True

        return False



