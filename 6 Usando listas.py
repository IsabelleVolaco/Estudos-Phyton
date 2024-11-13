print("Exercício criação de listas antes/depois")


prices = [10, 38, 40, 58, 62]
halved =[]

for price in prices:
    half_price = price/2
    halved.append(half_price)
print(halved)

#ou melhor...

prices = [10, 38, 40, 58, 62]
halved = [price/2 for price in prices]
print(halved)

#Uma criação de listas é uma maneira de criar uma nova lista como HALVED aplicando uma expressão em cada elemento de outra lista, como PRICES.







flights = ["1122", "5788", "0044"]

codes_a = ["BA" + flight for flight in flights]
print(codes_a) #resumido, mesmo resultado

codes_b = [] #maior, mesmo resultado
for flight in flights:
    code = "BA" + flight
    codes_b.append(code)
print(codes_b)







meters = [100, 3800, 4000]
kilometers = [m/100 for m in meters]
print(kilometers)


miles = [100, 57, 40, 20]
km = [value * 1609 for value in miles]
print(miles)
