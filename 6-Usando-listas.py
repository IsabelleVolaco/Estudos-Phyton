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



results = [3.12, 8.2, 7]
corrected = [result + 1 for result in results]
print(corrected)



prices = [10, 38, 40, 58, 62]
prices_copy = [price for price in prices] #aqui foi criada uma cópia da lista PRICES ao utilizar o [price for price] sem outras alterações.
print(prices_copy)



meters = [100, 3800, 4000]
meters_copy = [m for m in meters] #aqui foi criada uma cópia da lista METERS ao utilizar o [m for m] sem outras alterações.
print(meters)
print(meters_copy)



names = ["Winchester", "Masters", "John"]
prefixed = ["Mr." + name for name in names]
print(prefixed)



words = ["apple", "aligator", "abracadabra", "avatar"]
a_count = [word.count("a") for word in words]
print(a_count)




ages = [15, 20, 19]
can_drive = [age > 17 for age in ages]
print(can_drive)





print("Exercício criação de listas em funções - funções como expressões")


prices = [10, 22, 30, 40, 58, 62]
def halve(num):
    return num/2

halved = [halve(price) for price in prices]
print(halved)


# retirando o imposto antes de reduzir o preço pela metade
prices = [10, 22, 30, 40, 58, 60]
def halve(num):
    no_tax = 0.85 * num
    return no_tax/2

halved = [halve(price) for price in prices]
print(halved)




authors = ["Virginia Wolf", "Stephen King"]

def add_comma(name):
    parts = name.split(" ")
    return parts[1] + ", " + parts[0]

authors_update = [add_comma(name) for name in authors]
print(authors_update)




words = ["apple", "aligator", "abracadabra", "avatar"]

def has_double_a(word):
    count = word.count("a")
    return count == 2

double_a = [has_double_a(word) for word in words]
print(double_a)





scores = [40, 12, 83]

def passed(score):
    with_bonus = score + 10
    return with_bonus > 90

passing_scores = [passed(score) for score in scores]
print(passing_scores)





scores = [156, 70, 100]

def passed(score):
    with_bonus = score + 10
    passed = with_bonus > 90
    return passed

passing_scores = [passed(score) for score in scores]
print(passing_scores)






print("Exercício filtrando com expressões if")

scores = [12, 47, 30, 29, 19, 35]
high_scores = [score for score in scores if score > 20] #a nova lista irá conter somente os elementos filtrados (maiores que 20).
print(high_scores)



prices = [150, 45, 200, 340]
apply_taxes = [price for price in prices if price > 150]
print(apply_taxes)



item_prices = [120, 25, 40]
under_50 = [price for price in item_prices if price < 50]
print(under_50)




humidity = [40, 35, 20, 70]
too_low = [level for level in humidity if level < 30]
print(too_low)





humidity_percent = [40, 35, 20, 70]
ideal = [level for level in humidity_percent if level >= 30 and level <= 50]
print(ideal)





websites = ["nytimes.com", "lemonde.fr", "economist.com"]
french = [website for website in websites if website.count(".fr") > 0]
print(french)




book_codes = ["FH2010", "BV1999", "LB2010"]
books_2010 = [code for code in book_codes if code.count("2010") == 1]
print(books_2010)



print("Exercício indexação e exclusão negativa")

scores = [4.5, 5, 3, 4, 3.5, 4]
latest = scores[-1]
print(latest)


users = ["Tony", "Tina", "Tom"]
last = users[-1]
print(last)


ratings = [4, 5, 3, 1, 2, 3]
first = ratings[-6]
print(first)


# Ocorrerá um erro se for tentado recuperar um valor em uma posição fora do alcance do objeto.
"""     
results = ["Win", "Loss", "Draw"]
results[-5]
"""


user = ("Joe", "Paris", 27)
name = user[0]
age = user[-1]
message = f"{name} {age}"
print(message)



members = ["Anna", "Sarah", "Hayley", "Gareth"]
print(members[-3])


users = ["Peter", "Julia", "Irina"]
users[-1] = "Paul"
print(users)




print("Exercício indexação e exclusão negativa - usando DEL")

winners = ["John", "Ellen", "Sigmund", "Olaf"]
del winners[-1]
print(winners)


# Ao printar letters ocorrerá um erro, pois letters foi deletada.
"""
letters = {'a', 'b', 'c'}
del letters
print(letters)
"""


product = {'category': 'book',
           'price': 4.99,
           'in_shop': True
}
del product["in_shop"]
print(product)


orders = ['A', 'B', 'C']
del orders[-1]
print(orders)





print("Exercício slicing pt. I")
#sintaxe [start:stop]

ingredients = ["eggs", "flour", "sugar", "salt"] #start no mesmo indíce, stop no indíce anterior ao escolhido.
print(ingredients[0:2]) #start no indíce 0(eggs), será printado eggs; stop no indíce 2(sugar), mas será printado o indíce 1(flour).


letters = ["A","B","C","D","E"]
print(letters[4:]) #printado apenas 'E' pois iniciou em 4, e foi para -1, ambos equivalentes a 'E'.
print(letters[1:]) #printado todos menos 'A', pois iniciou em 'B', e foi para -1, deixando 0('A') de fora
print(letters[3:])


users = ["Alan", "Beth", "Carla", "Dennis"]
print(users[0:]) #printado todos pois foi de 0 a -1, de Alan a Dennis.
print(users[:]) #igual ao anterior.
print(users[-2:])


#especificar um intervalo fora do comprimento da lista resultará em uma lista vazia.
letters = ["A", "B", "C", "D", "E"]
print(letters[6:])


scores = [50, 40, 30, 20, 10]
print(scores[:2])
print(scores[2:4])


#um índice start depois do indíce stop no formato [start:stop] resultará em uma lista vazia.
animals = ['antelope', 'bear', 'cat', 'dog']
print(animals[3:0])



print("Exercício slicing pt. II")
#sintaxe [start:stop:step]

alphabet = ["A","B","C","D","E","F"]
print(alphabet[1:6:2]) #O resultado será B, D, F, pois começará em B, pulará dois indíces (step +2) imprimindo em D, pulando mais dois indíces (repetição step +2) até chegar no stop em 6(id.5 'F').


friends = ["Anna", "Bella", "Carrie", "Diana", "Eleanor"]
print(friends[::2]) #A resposta será essa pois inicia no id.0, step +2 até o id.2, step +2 até o id.4 o qual é a casa final para o stop 0(id.-1).


flowers = ["azaelea", "buttercup", "rose", "daffodil"] 
print(flowers[2::-1]) #a resposta será 2,1,0 pois tem start em id.2 (rose), imprime o step -1 (antehorário pois é negativo) até o id.1(butter.) e stop em 0(azaelea). 
print(flowers[:3:2]) # 0,2 pois start em id.0, step +2 até id.2 que é a casa stop requerida.


friends = ["Anna", "Bella", "Carrie", "Diana", "Eleanor"]
print(friends[3:0:-1]) #start em 3, dando step -1 e imprimindo até chegar no id.1 pois o stop é o 0.


scores = [100, 200, 300, 400, 500]
print(scores[0:2:-1]) #Resulta em uma lista vazia pois não há indíces correspondentes.
print(scores[4:1:-1])


countdown = ["3", "pause", "2", "pause", "1"]
numbers_only = countdown[::2]
print(numbers_only)


ratings = [3, 4, 2, 5, 1, 5, 4, 5]
print(ratings[-1:2:-2])


