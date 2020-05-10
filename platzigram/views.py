#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime
import json

def hello_world(request): 
    return HttpResponse('Hola charlie! La hora del server es: {now}'.format(
        now= datetime.now().strftime('%d/%m/%Y %H:%M hrs')
    ))        


def hi(request):
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
    