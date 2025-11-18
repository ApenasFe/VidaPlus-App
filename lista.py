from cadastro import list_dict
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def listar_pacientes():
    clear()
    print('Listando todos os pacientes por ordem de registro...')
    for client in list_dict:
        client_data = list_dict[client]
        print(f'| Nome: {client_data['nome']} | Idade: {client_data['idade']} | Telefone: {client_data['telefone']} |')
        time.sleep(0.2)
    input('Pressione Enter para continuar...')