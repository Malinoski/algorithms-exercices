"""
Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. 
Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. 
Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. 
Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. 
O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem
- Função para ler os valores (não recebe parâmetro e retorna os dois valores)
- Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
- Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
- Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)
"""

from dis import dis
from time import time


def get_user_input():
    time = float(input("Digite tempo em horas: "))
    speed = float(input("Digite velocidade média: "))
    return time, speed

def calc_distance(time:float, speed:float):
    return time * speed

def calc_liter(distance:float):
    return distance/12

def print_result(speed: float, time: float, distance: float, liters: float):
    """
    Print all results
    """
    print("Velociadade média: ", speed)
    print("Tempo gasto na viajem: ", time)
    print("Distancia percorrida: ", distance)
    print("Quantidade de litros utilizada na viagem: ", liters)

time, speed = get_user_input()
distance = calc_distance(time=time, speed=speed)
liters = calc_liter(distance=distance)
print_result(speed=speed, time=time, distance=distance, liters=liters)






