# mentor_app/decorators.py
from django.shortcuts import redirect
from django.contrib import messages

def status_required(required_status):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.userprofile.status != required_status:
                messages.warning(request, "Sul puudub sellele lehele ligipääs.")
                return redirect('home')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

def allowed_statuses(statuses):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.userprofile.status not in statuses:
                messages.warning(request, "Sul pole ligipääsu.")
                return redirect('home')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

