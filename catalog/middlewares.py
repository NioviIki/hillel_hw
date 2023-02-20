import json
from .models import SaveLogs


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)


        if "/admin/" not in request.path:
            if request.method == "GET":
                SaveLogs.objects.bulk_create([SaveLogs(
                    method_of_request=request.method,
                    path_of_request=request.path,
                    json_data=json.dumps(request.GET.dict())
                )])
            else:
                SaveLogs.objects.bulk_create([SaveLogs(
                    method_of_request=request.method,
                    path_of_request=request.path,
                    json_data=json.dumps(request.POST.dict())
                )])

        return response
