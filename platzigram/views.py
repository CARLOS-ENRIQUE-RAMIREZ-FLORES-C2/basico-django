#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime
import json

def hello_world(request): 
    """ Retorna un saludo y la hora del servidor"""
    return HttpResponse('Hola charlie! La hora del server es: {now}'.format(
        now= datetime.now().strftime('%d/%m/%Y %H:%M hrs')
    ))        


def sort_integers(request):
    """ Retorna  una respuesta en JSON de numero ordenados """
    """ Return a JSON response with sorted integers"""
    data = {}
    if 'numbers' in request.GET :
        numbers = [int(i) for i in request.GET['numbers'].split(',')]
        sorted_ints = sorted(numbers)
        data = {
            'status': 'ok',
            'numbers': sorted_ints,
            'message': "Integers sorted successfully"
        }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')
    
def say_hi(request, name, age):
    """ Return a greeating. """
    if age < 12:
        message =  "Sorry {name}, you are not allowed here!".format(name=name)
    else:
        message = "Hello, {}! Welcome to Platzigram.".format(name)
    
    return HttpResponse(message)
