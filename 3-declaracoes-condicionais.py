user_added = True
user = "Isabelle"

if user_added == False:
    print(f"Adding {user} to database")
else:
    print(f"Database has user {user}")

#------------------------------------------------
print("Exercício Uber")

ride_type = "Black"
credits = 4
ride_price = 0
final_price = 0

if ride_type == "UberX":
    ride_price = 20.5
elif ride_type == "Black":
    ride_price = 35.0
else:
    ride_price = 15.5
print(f"Ride price is: {ride_price}. Select credits option.")

if credits > 0:
    final_price = ride_price - credits
print(f"Credit applied! Final price: {final_price}")

#------------------------------------------------
print("Exercício de pontos")

minimum_points = 150
data_points = 100
if data_points >= minimum_points:
    print("Você pode comprar o item!")
if data_points < minimum_points:
    print(f"Você não tem pontos o suficiente! Faltam {minimum_points - data_points} pontos.")

#------------------------------------------------
print("Exercícios de permissão")

age = 17
has_permit = True

if age > 16 and has_permit:
    print("Can drive in US")

age = 17
has_permit = True

if age > 18 and has_permit == True:
    print("Can drive in Brazil")

age = 17
has_permit = True
is_insured = True

if age > 16 and has_permit and is_insured:
    print("Can drive. Os blocos de código serão pulados caso todos os requisitos não sejam cumpridos.")

"""
Comentários podem ser usados para não exibir parte do código.
print("este exemplo não irá aparecer")

"""
#print("e nem esse")

#------------------------------------------------
print("Exercício de notas or")

average_grade = "B"
final_score = 1400

if average_grade == "A" or final_score >= 1500:
    print("1# Certificate achieved!")

average_grade = "A"
final_score = 1400

if average_grade == "A" or final_score >= 1500:
    print("2# Certificate achieved!")

average_grade = "B"
final_score = 1600

if average_grade == "A" or final_score >= 1500:
    print("3# Certificate achieved!")

average_grade = "B"
final_score = 1400
won_competition = True

if average_grade == "A" or final_score >= 1500 or won_competition:
    print("4# Certificate achieved!")

average_grade = "B"
final_score = 1400
won_competition = False

if average_grade == "A" or final_score >= 1500 and won_competition:
    print("5# Certificate achieved!")

average_grade = "A"
final_score = 1400
won_competition = False

if average_grade == "A" or final_score >= 1500 and won_competition:
    print("6# Certificate achieved!")

average_grade = "A"
final_score = 1400
won_competition = True

if average_grade == "A" or final_score >= 1500 and won_competition:
    print("7# Certificate achieved!") 
