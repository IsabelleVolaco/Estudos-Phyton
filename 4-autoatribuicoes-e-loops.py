print("Exercício auto atribuição na carteira")
# O valor contido na carteira é de 500 reais. O usuário pode realizar saques ou depósitos por exemplo.

wallet = 500
wallet = wallet + 15
wallet = wallet - 10
print(wallet)

print("Exercício de nomes")

name = "Nome da conta: "
name = name + "Isabelle"
name = name + " Volaco"
name += " Babona"
print(name)

print ("Exercício autoatribuição de custo de frete")

international_shipping = True
total = 150
shipping_cost = 0

if international_shipping:
    shipping_cost += 15
    print("Preço base aplicado!")

if total <= 50:
    shipping_cost += 20

elif total <= 100:
    shipping_cost += 15

else:
    shipping_cost += 5

print(f"Shipping cost: {shipping_cost}")

print("Exercício loop while")

infinite = True
while infinite == True:
    print("8====D")
    infinite = False

contador = 0
while contador < 5:
    print("( . Y . )")
    contador = contador + 1

# O contador irá realizar o looping 5x até que atinja um número igual ou maior a 5.

contador = 1
while contador < 10:
    print(contador)
    contador += 1

print("Exercícios for")

for i in range(5):
    print("Exibir 5 vezes.")

for i in range(5):
    print(i)

for i in range(5):
    print(i)
    print("Exibir 5 vezes.")

print ("Exercício calculadora de juros bancários")

valor_inicial = 100
taxa_de_juros = 0.004
anos = 3
contador = 1

while contador <= anos:
    juros_acumulados = valor_inicial * taxa_de_juros
    valor_inicial += juros_acumulados
    print(f"Taxa: {valor_inicial}")
    contador += 1

valor_inicial = 100
taxa_de_juros = 0.004
anos = 3

for i in range(anos):
    juros_acumulados = valor_inicial * taxa_de_juros
    valor_inicial += juros_acumulados
    print(f"Taxa: {valor_inicial}")



print("Exercício cupom")

base = "netflix.com"
cupom = "login/cupom"
desconto = 50
quantia = 4

for num in range(quantia):
    print(f"{base}/{cupom}/{desconto}/{num}")
print(f"{quantia} cupons gerados!")


price = 100
discount = 10

for i in range(2):
    price = price - discount
    
print(f"Discount: {discount} - Price: {price}")
