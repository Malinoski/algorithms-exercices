"""
Leia a idade do usuário e classifique-o em:
- Criança – 0 a 12 anos
- Adolescente – 13 a 17 anos
- Adulto – acima de 18 anos
-Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida
"""

age = int(input("Digite um idade: "))

if age >= 0 and age <= 12:
    print("Criança")
elif age >= 13 and age <= 17:
    print("Adolescente")
elif age >= 18:
    print("Adulto")
else:
    print("Idade inválida")
