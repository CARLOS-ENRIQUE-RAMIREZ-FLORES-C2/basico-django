#Django
from django.http import HttpResponse
from django.http import JsonResponse
#Utilities
from datetime import datetime
import json

def hello_world(request): 
    return HttpResponse('Hola charlie! La hora del server es: {now}'.format(
        now= datetime.now().strftime('%d/%m/%Y %H:%M hrs')
    ))        


def hi(request):
    numbers = []
    if 'numbers' in request.GET :
        numbers = request.GET['numbers'].split(',')
    return JsonResponse(numbers, safe=False)
    