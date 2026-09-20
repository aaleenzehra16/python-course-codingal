print("Smart School Day Planner")
day=input("what is the day today?").strip().lower()
weather=input("how is the weather today?").strip().lower()
homework_status=input("Do you have homework today?").strip().lower()

print(f"Plan for {day}")
if day in ("saturday","sunday"):
    print("its a weekend, enjoy your day")
elif day == "monday":
    print("first day of school")
elif day == "friday":
    print("last day of school")
elif day in ("tuesday","wednesday","thursday"):
    print("regular school day")
else:
    print("day not recognised")

if weather == "sunny" and homework_status == "yes":
    print("hot weather, return home and complete homework")
if (weather == "cloudy" or weather == "rainy") and homework_status == "yes":
    print("Weather not suitable, take shade and complete your homework")
if weather == "cloudy" and not homework_status == "yes":
    print("good weather, go out and play")

if weather == "sunny" and homework_status == "yes":
    print("hot weather, return home and complete homework")
elif weather == "cloudy" or weather == "rainy" and homework_status == "yes":
    print("Weather not suitable, take shade and complete your homework")
elif weather == "cloudy" or weather == "sunny" and not homework_status == "yes":
    print("good weather, go out and play")
elif weather == "rainy" and not homework_status == "yes":
    print("take an umbrella when you go out!")
else:
    print("invalid imput for weather and homework")

print("Plan Complete! Have a wonderful day.")