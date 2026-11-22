def greet_customer():
    print("Welcome to the Art supplies store!")
    print("buy your colors, paints, brushes here!")
greet_customer()

price=float(input("enter the price for each art supply you purchased."))
item_count=int(input("enter the number of items you bought."))

def calculate_total(price,item_count):
    total=round(price*item_count,0)
    return(total)
total_cost=calculate_total(price,item_count)
print(total_cost)

paid=int(input("enter the total amount payed."))

def calculate_change(paid,total):
    change=round(total-paid,0)
    return(change)
change_due=calculate_change(paid,total_cost)
print(change_due)


def thankyou_message(item_count):
    if item_count>10:
        return("Thankyou for your support!")
    else:
        return("Thankyou for shopping at our store!")

print("-----Final Bill Receipt------")
print("Price:",price)
print("items bought:",item_count)
print("total cost:",total_cost)
print("amount paid:",paid)
print("change:",change_due)
print("Thankyou for visiting!")