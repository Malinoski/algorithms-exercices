"""
Crie uma lista vazia e faça a leitura de dois valores do tipo float, 
colocando cada um dos valores nas primeiras posições da lista (o valor1 ficará na posição 0 da lista e o valor2 ficará na posição 1 da lista). 
Faça a divisão dos dois valores e trate as seguintes exceções:
- ValueError: se o usuário digitar um caracter
- ZeroDivisionError: se o usuário digitar zero e ocorrer erro na divisão
- IndexError: caso a divisão seja feita levando em consideração posições que não existem na lista
- KeyboardInterrupt: caso o usuário interrompa a execução
"""

values_list = []
try:
    value1 = float(input("Digite valor 1: "))
    value2 = float(input("Digite valor 2: "))
    values_list.append(value1)
    values_list.append(value2)
    print("Result: ", (values_list[0]/values_list[1]))
    
except ValueError as ex:
    print("Erro: só é permitido números")
except ZeroDivisionError as ex:
    print("Erro: zero não é permitido")
except IndexError as ex:
    print("Erro: Index error")
except KeyboardInterrupt as ex:
    print("Erro: usuário interrompeu a execução!")
else:
    print("Fim")
