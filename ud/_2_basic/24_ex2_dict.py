# Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura dos valores por meio de uma estrutura de repetição. 
# Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média

# Get user imput and register in dict
qnt = 3
dict_users = {}
for element in range(qnt):
    print(f"==== User {element}")
    user_name = input(f"Digite nome aluno {element}:")
    user_note = int(input(f"Digite nota aluno {element}:"))
    dict_users[user_name] = user_note
print("Users: ", dict_users)

# Calculate users notes average
sum = 0
for name, value in  dict_users.items():
    sum += value
print("Média: ", sum/qnt)
    