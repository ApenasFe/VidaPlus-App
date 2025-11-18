from cadastro import list_dict
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#Função de busca
def buscar_paciente():
    client_found = False
    #Verifica o nome e trata caracteres inválidos
    while True:
        try:
            first_name = str(input('Digite o primeiro nome do paciente:\n')).capitalize()
            last_name = str(input('Digite o sobrenome do paciente\n')).capitalize()
            received_name = first_name + last_name
            if received_name.isalpha() == False:
                raise ValueError
            else:
                received_name = f'{first_name} {last_name}'
                break
        except ValueError:
            print('Deu um erro')
    #Itera sobre o dicionário em busca do nome recebido
    for client in list_dict:
        client_data = list_dict[client]
        if received_name == client_data['nome']:
            clear()
            print('Paciente encontrado!')
            print(f'Nome: {client_data['nome']}')
            print(f'Idade: {client_data['idade']}')
            print(f'Telefone: {client_data['telefone']}')
            client_found = True
            break
    #Condição para avisar que o usuário não foi encontrado
    if client_found == False:
        clear()
        print('Paciente não encontrado no sistema.')
    
    input('Pressione Enter para continuar...')
    clear()