"""
Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. 
A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius
- Função para ler e retorna o valor da temperatura (não recebe parâmetro)
- Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
- Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão
"""

def get_celsius_input():
    return float(input("Digite Celsius: "))

def convert_fahrenheit(celsius: float):
    return (9 * celsius + 160)/5

def print_temp(value: float):
    print("Resultdo: ", value)

calsius_value = get_celsius_input()
fahrenheit_value = convert_fahrenheit(calsius_value)
print_temp(fahrenheit_value)