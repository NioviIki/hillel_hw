import json

from .models import SaveLogs


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        if request.path[:6] != '/admin':
            SaveLogs.objects.create(
                method_of_request=request.method,
                path_of_request=request.path,
                query_data=request.GET.dict(),
                body_data=request.POST.dict()
            )

        return response
