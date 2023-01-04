import CRUD
import captcha


def menu():
    print("""
                MENU PRINCIPAL
        1 - CRUD
        2 - CAPTCHAS
        0 - Finalizar
    """)


while True:
    menu()
    switch = int(input("Digite a opção desejada: "))
    if switch == 1:
        CRUD.crud()
    elif switch == 2:
        captcha.captcha()
    elif switch == 0:
        break
    else:
        print('Error')
