"""
Pitch = https://drive.google.com/file/d/1SDOwpOPWGipPhLCBZfR0wP3FOcN2S8gy/view
"""
import functions as fc

while True:
    fc.menu()
    switch = int(input("Digite a opção desejada: "))
    if switch == 1:
        fc.new_register()
    elif switch == 2:
        id = int(input("Informe o código do cliente: "))
        fc.menu_change()
        campo = fc.verify_campo(int(input("Qual campo deseja altera? ")))
        fc.change_registration(id, campo)
    elif switch == 3:
        login = input("Login: ")
        passaword = input("Password: ")
        fc.master(login, passaword)
    elif switch == 4:
        print("Operação encerrada!")
        break
    else:
        print("Error")
