from django.http import HttpResponse
from datetime import datetime
import json

def hello(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Hello world!!! la hora actual en el servidor es {now}')

def numbers_sorted(request):
    listaNumbers = request.GET['numbers'].split(',')
    numbers = [int(number) for number in listaNumbers]
    sorted_numbers = sorted(numbers)
    data = {
        'status': 200,
        'numbers': sorted_numbers,
        'message': 'numeros ordenados correctamente'
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

def say_hi(request, name, age):
    if age < 12:
        message = f'Lo siento {name}, no puedes estar aqui' 
    else:
        message = f'Hola {name}, Bienvenido'
    
    return HttpResponse(message)