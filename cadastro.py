import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

list_dict = {
    "client1" : {
        'nome': 'Luis Silva',
        'idade': 22,
        'telefone': '(11) 96060-6060'
    },
    "client2" : {
        'nome': 'Maria Santos',
        'idade': 26,
        'telefone': '(11) 97070-7070'
    },
    "client3" : {
        'nome': 'João Pereira',
        'idade': 12,
        'telefone': '(11) 98080-8080'
    }
}
#Função de registro
def registrar_paciente():
    client_dict = {}
    register_number = 1
    #Recebe dado de nome do paciente
    client_name = ''
    #Verifica e formata o nome do paciente
    while True:
        try:
            first_name = input('Digite o primeiro nome do paciente\n').capitalize()
            if str(first_name).isalpha() == False:
                raise ValueError
            last_name = input('Digite o sobrenome do paciente\n').capitalize()
            if str(last_name).isalpha() == False:
                raise ValueError
            client_name = f'{first_name} {last_name}'
            break
        except ValueError:
            print('Nome inválido, apenas caracteres alfabéticos permitidos.')
    #Registra o nome do paciente no dicionário
    client_dict['nome'] = client_name
    clear()

    #Loop da função de verificação de dado
    while True:
        try:
            #Recebe dado da idade do paciente
            client_age = int(input('Digite a idade do paciente\n'))
            #Verifica o dado recebido
            if str(client_age).isnumeric() == False:
                raise ValueError
            elif client_age <= 0 or client_age > 122:
                raise ValueError
            else:
                break
        except ValueError:
            print('Idade inválida, digite apenas números.')
    #Registra a idade do paciente no dicionário
    client_dict['idade'] = int(client_age)
    clear()

    #Loop da função de verificação de dado
    while True:
        #Valida o dado recebido
        try:
            #Recebe dado de telefone do paciente
            client_phone = int(input('Digite o telefone do paciente\n'))
            #Verifica o dado recebido
            char_count = 0
            for _ in str(client_phone):
                char_count += 1
            if str(client_phone).isnumeric() == False:
                raise ValueError
            elif char_count != 11:
                raise ValueError
            else:
                break
        except ValueError:
            print('Número inválido, digite o DDD e número de telefone juntos, não pode exceder mais que 11 caracteres.')
    #Formata o número de telefone
    phone_ddd = str(client_phone)[0:2]
    phone_start = str(client_phone)[2:7]
    phone_end = str(client_phone)[7:11]
    formatted_number = f'({phone_ddd}) {phone_start}-{phone_end}'
    #Registra o número formatado
    client_dict['telefone'] = formatted_number
    #Adiciona o client_dict no list_dict
    while True:
        if f'client{register_number}' in list_dict:
            register_number += 1
        else:
            list_dict[f'client{register_number}'] = client_dict
            print(list_dict)
            break
    clear()
    #Exibe informações do paciente registrado
    print(f"""Paciente cadastrado
Nome: {client_name}
Idade: {client_age}
Telefone: {formatted_number}""")
    input('Pressione Enter para continuar...')
    clear()