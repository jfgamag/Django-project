from django.http.response import HttpResponse
from datetime import date, datetime


def hello_world(request):
    """Returns a greeting

    Args:
        request (HTTP):  Receives HTTP request

    Returns:
        Greeting: returns a greeting
    """
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh Hi! Current server time is {now}'.format(now=now))


def hi(request):
    """Returns hi

    Args:
        request (HTTP]): Returns simple hi
    """
    import pdb; pdb.set_trace()
    return HttpResponse("Hi")