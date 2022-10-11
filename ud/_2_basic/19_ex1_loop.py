"""
Ler 5 notas e informar a média
"""

i = 0
notes_sum = 0
qnt = 5
while i < qnt:
    notes_sum += int(input("Digite nota: "))
    i += 1
print("Média: ", notes_sum/qnt)
