temperature=int(input("what is the temperature today?")) #asking the temperature to recommend an outfit
if temperature < 20:
    outfit="jacket"
    print("it is cold today")
    print("wear",outfit)
else:
    outfit="t-shirt"
    print("it is normal today")
    print("wear a",outfit)

is_raining=input("is it raining today?")
if is_raining == "yes":
    print("take an umbrella")

wind_speed=int(input("what is the wind speed today"))
if wind_speed> 30:
    needs_windbreaker="yes" 
    print("it is windy today")
    print("wear a windbreaker on your",outfit)
else:
    needs_windbreaker="no"
    print("its normal today!")
    print("no windbreaker needed on your",outfit)

puddles=input("are there puddles on your way?")
if puddles == "yes":
    shoes="boots"
    print("the roads are wet.")
    print("wear",shoes)
else:
    shoes="sandals"
    print("the roads are dry.")
    print("wear",shoes)

print("the temperature is",temperature)
print("is it raining or not?",is_raining)
print("the wind speed is",wind_speed)
print(f"there are {puddles} on the road")