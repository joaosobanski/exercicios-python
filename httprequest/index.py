
#pip install requests
from unicodedata import category
import requests
import json
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

api_url = 'https://api.chucknorris.io/jokes'
endpoint_random = '/random'
endpoint_categories = '/categories'


isMenu = 1
showMenu = 1

categorias = 'nada encontrado'
 
response = requests.get(api_url + endpoint_categories)
if response.status_code == 200:
    categorias = json.loads(response.content) 

def caseCat():
    showMenu = 0
    print(categorias)

    back = input("Enter para voltar: ")
    if back:
        showMenu = 1

 


def caseGet():
    showMenu = 0 
    
    print(categorias)

    flag = 1
    while(flag):
        cat = input("Escolhar uma categoria: ")
        if cat in categorias:
            flag = 0  
            response = requests.get(api_url +endpoint_random+'?category='+cat)
            
            if response.status_code == 200:
                ret = json.loads(response.content) 
                print(ret['value'])

        else:
            print('Erro: Categoria válida!')

    back = input("Enter para voltar: ")
    if back:
        showMenu = 1
  
while isMenu:
    if showMenu:
        print('Escolha uma opção:')
        print('Lista de categorias : cat')
        print('Randomizar : get')
        print('sair')
        menu = input("Digite oque deseja fazer: ")

    match menu:
        case 'cat':
            cls()
            caseCat()
        case 'get':
            cls()
            caseGet()
        case 'sair':
            cls()
            print('Até mais...')
            isMenu=0
    