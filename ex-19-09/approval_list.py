"""
RM = 96302
Nome = Sara Leal de Moura Lessa
"""

approval_list = []

def menu():
    print("\nCadastro Disciplinas\n--------------------------\n0 - Sair\n1 - Cadastrar as disciplinas\n2 - Listar o registro\n\n")


def approval(n):
    if n >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"


def storage_approval():
    approval_dict = {}

    approval_dict["Disciplina"] = input("Disciplina........:")
    approval_dict["Média"] = float(input("Média............:"))
    approval_dict["Status"] = approval(approval_dict["Média"])

    approval_list.append(approval_dict)

    return approval_list


def record_list():
    for items in approval_list:
        print("{items['Disciplina']}%.25s| {items['Média']} |    {items['Status']}")


opc = 1

while opc != 0:

    menu()
    switch = int(input("Opção desejada: "))

    while not(switch == 1 or switch == 2 or switch == 0):
        print("Opção inválida, por favor escolha entre 0, 1 ou 2")
        switch = int(input("Opção desejada: "))

    if switch == 1:
        print("Cadastrar Com As Notas\n----------------------------------\n")
        storage_approval()

    elif switch == 2:
        print("Disciplinas           MF    Status\n------------------------------------------")
        record_list()

    opc = switch