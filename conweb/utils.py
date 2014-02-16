from django.core.exceptions import PermissionDenied

def require_group(group_name):

    if not isinstance(group_name, basestring):
        raise TypeError("Group name must be a string.")

    def _wrap(view_func):
        def _func(request, *args, **kwargs):
            user = request.user
            if user.is_superuser or user.groups.filter(name=group_name):
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied("Permission Denied.")
        return _func
    return _wrap
