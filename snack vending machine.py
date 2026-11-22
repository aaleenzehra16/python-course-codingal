#Snack vending machine
#this program is used to create a vending machine that accepts coins and gives change

def calculate_change(paid,price):
    change=paid-price
    return change

snack_price=50
print("Vending machine")
print("snack cost:",snack_price)
print("accepted coin values:1,5,10,25")

total_inserted=0
coins_inserted=0

while True:
    coin=int(input("insert a coin"))
    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("invalid coin")
        continue
    total_inserted+=coin
    coins_inserted+=1
    print(coins_inserted)
    print(total_inserted)
    if total_inserted>=snack_price:
        print("enough money was inserted")
        break
change_due=calculate_change(total_inserted,snack_price)
print(change_due)
print("snack is being dispensed")

if change_due ==0:
    pass
else:
    print(change_due)