secret=28
attempts=0
guess=int(input("enter a number between 1 and 50"))
while guess>=1 or guess<=50:
  while attempts<=5:
    guess=int(input("enter a number between 1 and 50"))
    if guess<15 or guess>40:
      print("wrong guess, hint:ice cold!")
    elif guess>15 and guess<20 or guess<40 and guess>35:
      print("wrong guess, hint:cold!")
    elif guess>20 and guess<25 or guess<35 and guess>30:
      print("wrong guess, hint:warm!")
    elif guess>25 and guess<secret or guess<30 and guess>secret:
      print("wrong guess, hint:hot!")
    else:
      print("correct guess, you won!")
if attempts>5:
  print("you lost the game!")
  print("the secret number was",secret)
