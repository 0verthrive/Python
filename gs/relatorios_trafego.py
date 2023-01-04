
import random
from datetime import datetime
import time
import json

proporcao_veiculos = {}
lista_dicio = []
abriu = 0
aleatorios = 0, 1, 2, 3
aleatorio = 0, 1
seconds = 0
abriu = 0

for trafego in range(5):
    veiculos = [random.choice(aleatorios) for i in range(random.randint(1, 20))]
    pedestres = [random.choice(aleatorio) for i in range(random.randint(1, 20))]

    dicio = {
        'pedestres': pedestres,
        'veiculos': veiculos
    }
    lista_dicio.append(dicio)
    seconds += time.time()
    time.sleep(2)


def count_p():
    counts = 0
    q_pedestres = 0
    global abriu
    for i in lista_dicio:
        for key, value in i.items():
            if key == 'pedestres':
                for j in value:
                    if j == 1:
                        counts += 1
                        q_pedestres += 1
                if counts >= 8:
                    abriu += 1
        counts = 0
    return q_pedestres


def count_v():
    counts = 0
    moto = 0
    grandes = 0
    carro = 0
    ocioso = 0

    for i in lista_dicio:
        for key, value in i.items():
            if key == 'veiculos':
                for j in value:
                    if j == 1:
                        moto += 1
                        counts += 1
                    elif j == 2:
                        carro += 1
                        counts += 1
                    elif j == 3:
                        grandes += 1
                        counts += 1
                    else:
                        ocioso += 1
                        counts += 1

    proporcao_veiculos = {
        'data&hora': datetime.now().strftime('%d/%m/%Y %H:%M'),
        'segundos': seconds,
        'ocioso': f'{(ocioso/counts)*100:00.2f}%',
        'motos': f'{(moto/counts)*100:00.2f}%',
        'carros': f'{(carro / counts) * 100:00.2f}%',
        'veiculos_grandes': f'{(grandes / counts) * 100:00.2f}%'
    }
    return proporcao_veiculos


control_farol = {
    'data&hora': datetime.now().strftime('%d/%m/%Y %H:%M'),
    'segundos': seconds,
    'quantidade_pedestres': count_p(),
    'abertura_farol': abriu,
    'media_abertura': f'{abriu / 60:00.4f}'
}


with open('relatorio.txt', 'a') as file:
    valores_relatorio = [control_farol['data&hora'], control_farol['segundos'], control_farol['abertura_farol'], control_farol['media_abertura']]
    for i in valores_relatorio:
        file.write(f'{json.dumps(i)}\n')

    file.close()


def ler_relatorio():
    with open('relatorio.txt', 'r') as file:
        lista = ['Data e Hora', 'Tempo de duração (s)', 'Quantidade de aberturas', 'Média de abertura (min)']
        indice = 0
        for i in file:
            print(f'{lista[indice]} = {i}')
            indice += 1
            if indice >= len(lista):
                indice = 0
        file.close()


ler_relatorio()
