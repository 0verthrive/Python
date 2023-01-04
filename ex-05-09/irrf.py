'''
# Exercício calculo IRRF
#     até 1.903,98 = isento - isento
#     até 2.826,65 = 7,5% - 142,80
#     até 3.751,05 = 15% - 354,80
#     até 4.664,68 = 22,5% - 636,13
#     ↑   4.664,68 = 27,5% - 869,36
'''

faixaSalarial = (1903.98, 2826.65, 3751.05, 4664.68, 4664.69)
porcentDesc = (7.5, 15, 22.5, 27.5)
deducao = (142.80, 354.8, 636.13, 869.36)
salary = float(input("Informe seu salário: "))

if salary <= faixaSalarial[0]:
    print("Você está isento da tarifa!")

elif salary <= faixaSalarial[1]:
    valueFinal = (salary * (porcentDesc[0] / 100)) - deducao[0]
    print(f'Salario: {salary}\nAliquota: {porcentDesc[0]}%\nDedução: {deducao[0]}')
    print('Tarifa: %.1f' % abs(valueFinal))

elif salary <= faixaSalarial[2]:
    valueFinal = (salary * (porcentDesc[1] / 100)) - deducao[1]
    print(f'Salario: {salary}\nAliquota: {porcentDesc[1]}%\nDedução: {deducao[1]}')
    print('Tarifa: %.2f' % valueFinal)

elif salary <= faixaSalarial[3]:
    valueFinal = (salary * (porcentDesc[2] / 100)) - deducao[2]
    print(f'Salario: {salary}\nAliquota: {porcentDesc[2]}%\nDedução: {deducao[2]}')
    print('Tarifa: %.2f' % valueFinal)

elif salary >= faixaSalarial[4]:
    valueFinal = (salary * (porcentDesc[3] / 100)) - deducao[3]
    print(f'Salario: {salary}\nAliquota: {porcentDesc[3]}%\nDedução: {deducao[3]}')
    print('Tarifa: %.2f' % valueFinal)

else:
    print('fail')
