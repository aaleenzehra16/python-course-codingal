try:
    num1=int(input("enter a number."))
    num2=int(input("enter a number"))
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("division by zero is error !!")
except SyntaxError:
    print("the correct input format is:1,2")
except:
    print("wrong input")
finally:
    print("this will execute no matter what.")
    