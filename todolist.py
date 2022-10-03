import pymongo
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["python"]

dblist = myclient.list_database_names()

print(dblist)

if "mydatabase" in dblist:
  print("The database exists.")

mycol = mydb["todolist"]
collist = mydb.list_collection_names()
if "todolist" in collist:
  print("The collection exists.")

isMenu = 1

showMenu = 1

def buscar():
    print('buscarr')
    showMenu = 0

    mydoc = mycol.find()
    
    for x in mycol.find():
        print(x)

    back = input("Digite para voltar: ")
    if back:
        showMenu = 1

def inserir(): 
    showMenu = 0 
    title = input("Informe o titulo: ")
    mydict = { "title": title  }
    mydoc = mycol.find_one(mydict)

    if mydoc:
        newvalues = { "$set": mydict }
        mycol.update_one(mydict, newvalues)
    else:
        mycol.insert_one(mydict) 
    novo = mycol.find_one(mydict)
    
    print(novo)
    
    back = input("Digite para voltar: ")
    if back:
        showMenu = 1

def deletar():
    showMenu = 0

    title = input("Informe o titulo que deseja deletar: ")

    mydict = { "title": title  }

    mycol.delete_one(mydict)
    
    print(title + ' Foi removido')
     
    back = input("Digite para voltar: ")
    if back:
        showMenu = 1
        
while(isMenu==1):
    cls()
    if showMenu: 
        print('Opções do menu:')
        print('buscar')
        print('inserir')
        print('deletar')
        print('sair')
        menu = input("Digite oque deseja fazer: ")

    match menu:
        case 'buscar':
            cls()
            buscar()
        case 'inserir':
            cls()
            inserir()
        case 'deletar':
            cls()
            deletar()
        case 'sair':
            cls()
            print('Até mais ...')
            isMenu = 0
            







