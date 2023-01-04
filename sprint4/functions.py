import random as rd
import json
list_global = []
tupla_access = ("Admin", "master123")


# menus
def menu():
    print('''
        Esse é um canal ajuda rápida, como posso ajudar:
        1 - Cadastrar
        2 - Alterar Cadastro
        3 - _Master_
        4 - Sair
    ''')


def menu_change():
    print('''
        1 - Nome
        2 - Sobrenome
        3 - Celular
        4 - Idade
    ''')


# Escreve os dados do cliente no arquivo txt
def save_clients(reg):
    with open('clients.txt', 'w') as file:
        for i in reg:
            file.write(json.dumps(i)+'\n')
        file.close()


# Daqui até antes do próximo comentário pertence ao cadastramento de novos clientes.
def generator_id():
    return rd.randint(0, 999)


def verify_year(idade):
    if idade <= 17 or idade > 120:
        return True


def new_register():
    dicio = {
        'Id': generator_id(),
        'Nome': input("Nome: "),
        'Sobrenome': input("Sobrenome: "),
        'Celular': input("Celular: ")
    }

    idade = int(input("Idade: "))
    while verify_year(idade):
        print("Idade não está em conformidade")
        idade = int(input("Idade: "))
    else:
        dicio['Idade'] = idade
        list_global.append(dicio)
        save_clients(list_global)
    print(f'Cadastro realizado com sucesso:\n{dicio}\n')


# Mudanças no cadastro do cliente
def verify_campo(campo):
    if campo == 1:
        return 'Nome'
    elif campo == 2:
        return 'Sobrenome'
    elif campo == 3:
        return 'Celular'
    elif campo == 4:
        return 'Idade'
    else:
        print('Error')


def change_registration(id, campo):
    with open('clients.txt', 'r+') as file:
        for i in list_global:
            for key, value in i.items():
                if value == id:
                    i[campo] = input("Digite o novo valor desejado:")
        save_clients(list_global)
        file.close()


# Acesso master de listagem
def master(login, psw):
    if login == tupla_access[0] and psw == tupla_access[1]:
        print("Lista de clientes:")
        with open('clients.txt', 'r') as file:
            for i in file:
                print(i)
    else:
        print("Acesso negado!")
