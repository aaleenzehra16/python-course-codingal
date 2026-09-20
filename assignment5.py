#asking the temperature to recommend a suitable activity
temperature=int(input("what's the temperature today?"))
if temperature>20:
    activity="indoor reaading"
    print("too hot",activity,"is recommended")
else:
    activity="outdoor play"
    print("suitable temperature",activity,"is recommended")

#sending a reminder for rainy weather
rain_status=input("is it raining today?")
if rain_status == "yes":
    print("reminder: its raining today")
else:
    print("no rain, feel free to go outside")

#advising a suitable break between studying
homework_time=int(input("How many minutes did you spend on your homework?"))
if homework_time>45:
    study_break="suggested" 
    print("it is",study_break,"to take a break")
else:
    study_break="not suggested"
    print("break is",study_break,"continue studying")

#recommeding how to spend free time to the user
free_time=input("Do you have free time?")
if free_time == "yes":
    hobby="netflix"
    print("spend your free time watching",hobby)
else:
    hobby="planning your schedule"
    print("you dont have much freetime, try",hobby)

#printing the final summary
print("Daily Activity Planner")
print("Temperature:",temperature,", Activity recommended:",activity)
print("Rain Status:",rain_status)
print("Study Break:",study_break)
print("Hobby recommended:",hobby)