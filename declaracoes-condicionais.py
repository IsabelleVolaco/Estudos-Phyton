user_added = True
user = "Isabelle"

if user_added == False:
    print(f"Adding {user} to database")
else:
    print(f"Database has user {user}")

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
