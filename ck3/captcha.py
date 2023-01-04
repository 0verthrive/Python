import random as rd


def captcha():

    listaGlobal = []

    def create_file():
        with open('captchas.txt', 'w') as files:
            for i in listaGlobal:
                files.write(f'{str(i)}\n')

            files.close()

    def read_file():
        with open('captchas.txt', 'r') as files:
            for i in files:
                print(i)
            files.close()

    def file_captchas():
        create_file()
        read_file()

    def tipos(esc, qtd):
        alfanum = cara()
        opc = esc.split(' ')
        lista = []

        for i in opc:
            if i == 'l':
                for j in alfanum[0]:
                    if j == j.lower() and not(j.isdigit()):
                        lista.append(j)
            elif i == 'L':
                for j in alfanum[0]:
                    if j == j.upper():
                        if not(j.isdigit()):
                            lista.append(j)
            elif i == 'd':
                for j in alfanum[0]:
                    if j.isdigit():
                        lista.append(j)
            elif i == 'e':
                for j in alfanum[1]:
                    lista.append(j)
            else:
                print('Não está entrando em nenhum')
        captch = ''.join(rd.sample(lista, qtd))
        listaGlobal.append(captch)
        return captch

    def qtd_caracters(qtd):
        alfa = cara()
        captch = ''.join(rd.sample(alfa[0]+alfa[1], qtd))
        return captch

    def captcha_random():
        alfanum = cara()
        captch = ''.join(rd.sample(alfanum[0]+alfanum[1], 10))
        return captch

    def cara():
        alfanum = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', '0'
        ]
        especial = ['@', '#', '!', '$', '%', '&', '*', '_', '-']
        forall = [alfanum, especial]

        return forall

    def menu_v3():
        print("""
            [l]etras minúsculas
            [L]etras maiúsculas
            [d]ígitos 
            [e]speciais
        """)

    def menu():
        print("""
            1 - Gerar captcha aleatório
            2 - Escolher a quantidade de caracteres
            3 - Escolher Tipo de caracter
            4 - Ler lista de captchas
            5 - Gravar/Ler arquivo de captchas
            6 - Voltar
        """)

    while True:
        menu()
        switch = int(input("Qual operação deseja fazer: "))

        if switch == 1:
            print(captcha_random())
        elif switch == 2:
            print(qtd_caracters(int(input("Informe a quantidade de caracteres: "))))
        elif switch == 3:
            menu_v3()
            escolha = input("Quais opções você gostaria? ")
            print(tipos(escolha, int(input("Quantidade de caracteres: "))))
        elif switch == 4:
            print(listaGlobal)
        elif switch == 5:
            file_captchas()
        elif switch == 6:
            break
