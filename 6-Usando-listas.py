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



answers = [True, False, False] 
opposite = []
for answer in answers:
    opposite.append(not answer)
print(opposite) #maior, mesmo resultado


answers = [True, False, False] 
print([not answer for answer in answers]) #resumido, mesmo resultado






expiry_years = [2018, 2020, 2019]
renewed = [year + 4 for year in expiry_years]
print(renewed)






ages = [15, 20, 19]
can_drive = [age >= 18 for age in ages]
print(can_drive)




ages = [15, 20, 19]
can_drive = [age > 17 for age in ages]
print(can_drive)
