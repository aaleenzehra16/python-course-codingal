#swimming pool entry checker
print("Swimming Pool Entry Check")
print("Go through the survey to enter the pool!")
age=0
can_swim=input("can you swim?")
if can_swim == "yes": #asking for details if the guests can swim
   age=(int(input("Enter your age.")))
   height=(int(input("Enter your height in cm.")))
elif can_swim == "no":
   print("Sorry! You are not allowed to swim in any of the swimming pools. Feel free to dip your feet and enjoy.")
elif not can_swim == "yes" and not can_swim == "no": #checking for errors while answering the questions
   print("Error identified, start the survey again.")

adult=0 #seeing if guests are accompanied by an adult
if age<18:
   adult=input("Are you accompanied by an adult?").strip().lower()
print("Survey ended, Kindly wait!")

#sorting the guests into age groups
if age<4 and can_swim == "yes":
   print("Toddler: Splash pool only, an adult is to be accompanied with.")
elif age<12 and can_swim == "yes":
   print("Child: main pool with an adult.")
elif age<18 and can_swim == "yes":
   print("Teen: main pool alone")
elif can_swim == "yes":
   print("Adult: all pools allowed except the splash pool.")

#entry check for the deep pool
if can_swim == "yes" and adult == "yes" or age>18:
   print("You are allowed to enter the deep pool.Enjoy!")

#warning to watch out for shallow ends
if age<2 or can_swim == "no":
   print("beware of the shallow ends.")

#reminder for the prescence of a lifeguard
if adult == "no":
   print("lifeguard present nearby! seek help when needeed.")

#final message
if can_swim == "yes":
   print("Have a safe swim!")