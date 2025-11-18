import os
from cadastro import registrar_paciente
from estatisticas import exibir_estatisticas
from busca import buscar_paciente
from lista import listar_pacientes

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

menu = """=== SISTEMA CLÍNICA VIDA+ ===
1. Cadastrar paciente
2. Ver estatísticas
3. Buscar paciente
4. Listar todos os pacientes
5. Sair"""

while True:
    print(menu)
    user_choice = int(input('Digite o número de uma das opções\n'))
    match user_choice:
        case 1:
            clear()
            registrar_paciente()
        case 2:
            clear()
            exibir_estatisticas()
        case 3:
            clear()
            buscar_paciente()
        case 4:
            clear()
            listar_pacientes()
        case 5:
            clear()
            print('Saindo do programa...')
            break
        case _:
            clear()
            print('Não é uma opção válida')