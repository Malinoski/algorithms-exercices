# Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. 
# Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados

# Get user values and append in list
list = []
qnt = 5
for colect in range(qnt):
    value = int(input("Digite valor:"))
    list.append(value)

# Sum values
sum_result = 0
count = 0
while count < qnt:
    sum_result += list[count]
    count += 1
print("Soma total: ", sum_result)