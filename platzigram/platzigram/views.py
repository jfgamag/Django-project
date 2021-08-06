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


def sort_n(request):
    
    numbers = request.GET['numbers'].split(',')
    ord_numb = sorted([int(i) for i in numbers])
    data = {
        'status': 'OK',
        'numbers': ord_numb,
        'Message': 'Integer sorted succesfully'
    }
    return JsonResponse(data)
    
