import logging
import datetime

logger = logging.getLogger(__name__)

class RequestWatchMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the incoming request with additional information
        timestamp = datetime.datetime.now()
        method = request.method
        path = request.path
        query_params = request.GET.dict()
        body_params = request.POST.dict()
        headers = dict(request.headers)

        logger.info(f"[{timestamp}] {method} {path} Query Params: {query_params} Body Params: {body_params} Headers: {headers}")

        response = self.get_response(request)

        return response