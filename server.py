import sys
import requests


def menu() -> None:
    print("Добро пожаловать в нашу игру кликер!")
    print("[1] Войти")
    print("[2] Зарегистрироваться")
    print("[3] Выход")
    choice = input("Введите пункт: ")
    while not choice.isdigit():
        print("Некорректный ввод, повторите...")
        choice = input("Введите пункт: ")
    choice = int(choice)
    while not 1 <= choice <= 3:
        print("Некорректный пункт меню, выход...")
        sys.exit()
    match choice:
        case 1:
            return login()
        case 2:
            return register()
        case 3:
            sys.exit()

def login() -> str:
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    response = requests.get(f"http://localhost:8080/login/{login}/{password}").json()
    if response['status'] == 200:
        return login
    
def register() -> str:
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    response = requests.get(f"http://localhost:8080/register/{login}/{password}").json()
    print(response['message'])
    return menu()

def get_score(login: str) -> int:
    response = requests.get(f"http://localhost:8080/get_score/{login}").json()
    return response['score']

def add_score(login: str, value: int) -> None:
    requests.get(f"http://localhost:8080/add_score/{login}/{value}").json()
    
def reduce_score(login: str, value: int) -> None:
    requests.get(f"http://localhost:8080/reduce_score/{login}/{value}").json()
    
def add_animal(login: str, kind: str) -> None:
    response = requests.get(f"http://localhost:8080/add_animal/{login}/{kind}").json()
    return response['name']

def get_animals(login: str) -> None:
    response = requests.get(f"http://localhost:8080/get_animals/{login}").json()
    return response