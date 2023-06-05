import logging
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def index(request):
    for key, value in request.POST.items():
        logger.info(f"POST param: {key}={value}")

    if request.GET.get("key") == "test":
        return HttpResponse("Posts with test key")

    return HttpResponse("Posts index view")