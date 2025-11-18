from cadastro import list_dict
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_estatisticas():
    #Numero total de pacientes e idade
    total_client = 0
    total_age = 0
    age_list = []
    min_age = 0
    max_age = 0
    younger_client = ''
    oldest_client = ''
    #Iteração no dicionário para calculos de idade
    for client in list_dict:
        total_client += 1
        client_age = list_dict[client]['idade']
        total_age += client_age
        age_list.append(client_age)
    min_age = min(age_list)
    max_age = max(age_list)
    average_age = total_age / total_client
    #Iteração no dicionário para consultar dados de acordo com a idade mínima e máxima
    for client in list_dict:
        client_data = list_dict[client]
        actual_age = client_data['idade']
        if min_age == actual_age:
            younger_client = client_data['nome']
        if max_age == actual_age:
            oldest_client = client_data['nome']
    #Exibe o total de pacientes registrados
    print(f'Total de pacientes registrados: {total_client}')
    #Exibe a média de idade dos pacientes registrado
    print(f'Média de idade dos pacientes registrados: {int(average_age)} anos.')
    #Exibe o paciente mais novo registrado.
    print(f'Paciente mais novo registrado: {younger_client} ({min_age} anos)')
    #Exibe o paciente mais velho registrado.
    print(f'Paciente mais velho registrado: {oldest_client} ({max_age} anos)')
    input('Pressione Enter para continuar...')
    clear()