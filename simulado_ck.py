# Sabemos que um triângulo tem 3 lados.
# Não necessariamente por este motivo, ter 3 lados, ele é um triângulo.
# Para ser um triangulo um lado deve ser menor que a soma dos outros dois, nas 3 óticas.
# Caso tenhamos certeza que os lados formam um triângulo, temos que decidir de qual tipo é este triângulo. Seguem os critérios:
# - Equilátero: os três lados são iguais.
# - Isósceles: 2 lados são iguais.
# - Escaleno: 3 lados diferentes.
# Crie uma solução que pegue três valores fornecidos pelo usuário e diga, se for um triângulo, qual ele é.
# A cada verificação, pergunte se o usuário deseja continuar executando o programa, sendo 1 para Sim ou 2 para Não. Números diferentes deste, advertir e pedir um destes números.
# Esta solução deve ser desenvolvida com o conceito de subalgoritmos onde for possível, lembrando que cada subalgoritmo deve ser atômico, ou seja, cada um resolve um problema.

print('informe os 3 lados')
l1= float(input('Lado 1: '))
l2= float(input('Lado 2: '))
l3= float(input('Lado 1: '))

if (l1+l2) > l3 and (l3+l2) > l1 and (l3+l1) > l2:
    if l1 == l2 and l2 == l3:
        print('Triângulo equilátero')
    elif (l1 == l2 and l1 != l3) or (l2 == l3 and l2 != l1):
        print('triangulo isósceles')
    else:
        print('Triângulo escaleno')

else:
    print('Não é um triângulo')