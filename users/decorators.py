from django.http import HttpResponse
from functools import wraps

def role_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):

            # If user is not logged in
            if not request.user.is_authenticated:
                return HttpResponse("Login required")

            # Get role safely
            user_role = request.user.profile.role

            # Check permission
            if user_role not in allowed_roles:
                return HttpResponse(
                    f"Access Denied! Your role '{user_role}' is not allowed."
                )

            return view_func(request, *args, **kwargs)

        return wrapper
    return decorator


