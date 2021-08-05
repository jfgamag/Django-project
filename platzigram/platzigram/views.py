from django.http.response import HttpResponse
from datetime import date, datetime


def hello_world(request):
    """Returns a greeting

    Args:
        request (HTTP):  Receives HTTP request

    Returns:
        Greeting: returns a greeting
    """
    now = datetime.now()
    return HttpResponse('Oh Hi! Current server time is {now}'.format(now=str(now)))