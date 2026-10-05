#Custom Ride Builder
#Nested Conditional Statements

print("----Ride Builder----")
print()

print("press 1 for bike")
print("press 2 for car")
option=input("Choose 1 or 2")

if option=="1":
    print("you have chosen the bike")
    print("choose 1 for scooty")
    print("choose 2 for mountain bike")
    bike_type=input("choose 1 or 2")
    if bike_type=="1":
        print("chosen scooty")
        print("speed: 40km/h")
        print("Best used for internal commute")
    else:
        print("chosen mountain bike")
        print("speed:80km/h")
        print("Best for adventures")
elif option=="2":
    print("you have chosen the car")
    print("choose 1 for Sedan")
    print("choose 2 for SUV")
    car_type=input("choose 1 or 2")
    if car_type=="1":
        print("chosen Sedan")
        print("5 seater")
        print("best used city commute")
    else:
        print("chosen SUV")
        print("5 seater")
        print("best used for city to city travel")
else:
    print("invalid choice")
    print("enter either 1 or 2")

print("#########################")
print(" Enjoy your custom ride")
print("#########################")




