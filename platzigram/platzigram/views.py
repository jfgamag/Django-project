from django.http.response import HttpResponse
from datetime import datetime
from django.http import JsonResponse


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
    numbers = request.GET['numbers'].split(',')
    ord_numb = sorted([int(i) for i in numbers])
    return JsonResponse(ord_numb, safe=False)
    
