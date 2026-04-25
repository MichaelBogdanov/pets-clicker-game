from random import choice
from django.http import JsonResponse
from .models import *

# Create your views here.
def register(request, login, password):
    if not User.objects.filter(login=login).exists():
        user = User()
        user.login = login
        user.password = password
        user.save()
        return JsonResponse({'status': 200, 'message': 'Пользователь успешно зарегистрирован'})
    else:
        return JsonResponse({'status': 401, 'message': 'Пользователь с таким логином уже существует'})
    
def login(request, login, password):
    data = {}
    if User.objects.filter(login=login).exists():
        user = User.objects.get(login=login)
        if user.password == password:
            data['status'] = 200
            data['message'] = 'Пользователь успешно авторизован'
        else:
            data['status'] = 401
            data['message'] = 'Неверный пароль пользователя'
    else:
        data['status'] = 404
        data['message'] = 'Пользователь не найден'
    return JsonResponse(data)
    
def get_score(request, login):
    user = User.objects.get(login=login)
    return JsonResponse({'status': 200, 'score': user.score})
    
def add_score(request, login, value):
    user = User.objects.get(login=login)
    user.score += value
    user.save()
    return JsonResponse({'status': 200, 'message': 'Счёт успешно обновлен'})

def reduce_score(request, login, value):
    user = User.objects.get(login=login)
    user.score -= value
    user.save()
    return JsonResponse({'status': 200, 'message': 'Счёт успешно обновлен'})

def add_animal(request, login, kind):
    animal = Animal()
    animal.name = choice(Name.objects.all())
    animal.kind = Kind.objects.get(name=kind)
    animal.user = User.objects.get(login=login)
    animal.save()
    return JsonResponse({'status': 200, 'message': 'Животное успешно добавлено', 'name': animal.name.name})

def get_animals(request, login):
    user = User.objects.get(login=login)
    animals = Animal.objects.filter(user=user)
    return JsonResponse([(animal.name.name, animal.age, animal.kind.name, animal.kind.life_duration) for animal in animals], safe=False)