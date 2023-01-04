def crud():
    lista = []

    def add():
        while True:
            dicio = {}
            dicio['Apelido'] = input("Apelido: ")
            dicio['Nome'] = input("Nome: ")
            dicio['Sexo'] = input("Sexo: ")
            dicio['Telefone'] = input("Telefone: ")

            lista.append(dicio)

            opc = input("Deseja adicionar mais contatos? [S]im ou [N]ão")
            opc.upper()
            if opc == 'N':
                break

    def edit():
        older_value = input("Digite o valor que deseja alterar: ")
        new_value = input("Digite o novo valor: ")
        for i in lista:
            for key, values in i.items():
                if values == older_value:
                    i[key] = new_value

    def search(value):
        for i in lista:
            for key, values in i.items():
                if values == value:
                    print(f'\n{i}')

    def contact_list():
        for i in lista:
            print(f'\n{i}')

    def delete(value):
        for i in lista:
            print(i)
            for key, values in i.items():
                if values == value:
                    lista.remove(i)
                    print(f"Remoção completa\n{lista}")
                    break

    def switch(opc):
        if opc == 1:
            add()
        elif opc == 2:
            edit()
        elif opc == 3:
            value = input("Informe o valor desejado: ")
            search(value)
        elif opc == 4:
            contact_list()
        elif opc == 5:
            value = input("Informe o contato que deseja remover: ")
            delete(value)
        elif opc == 6:
            return 6

    def menu():
        print('''
            1 - Adicionar novo contato
            2 - Editar um contato
            3 - Pesquisar contato
            4 - Listar contatos
            5 - Apagar um contato
            6 - Sair
        ''')

    while True:
        menu()
        swit = switch(int(input('Digite o número da ação desejada: ')))
        if swit == 6:
            break
