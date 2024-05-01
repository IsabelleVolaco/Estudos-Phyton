"""Exemplo de listas"""

pizza = ["pepperoni","siciliana","milho com bacon"]
print(pizza)

pizza = ["pepperoni","siciliana","milho com bacon"]
print(pizza[0])

pizza = ["pepperoni","siciliana","milho com bacon"]
print(pizza[2])

pizza = ["pepperoni","siciliana","milho com bacon"]
pizza[2] = "4 queijos"
print(pizza)

#Os valores de uma lista são chamados de elementos. A posição dos elementos na lista é o índice (0,1,2 = 3).

print("exercícios de instruções")

mercado = []
mercado.append("tomate")
print(mercado)

mercado.insert(0, "leite")
print(mercado)

mercado.pop(1)
print(mercado)



nomes = ["josué","carlinhos","mario"]
nomes.append("amanda")
print(nomes)

nomes = ["josué","carlinhos","mario"]
nomes.insert(1,"amanda")
print(nomes)

nomes.pop()
print(nomes)



hamburguer = ["cheddar","cebola","tomate","alface"]
remover = hamburguer.pop(2)
print(hamburguer)



print("uso de for nas listas")

final_score = [5,3,6,10,8]
for score in final_score:
    print(score)

partida = ["juninho", "samanta", "bruno"]
for jogadores in partida:
    print(jogadores)
    print("----")
