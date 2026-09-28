v,w,x,y = 5,2,3,4
z =  (v + w) * x / y
print (z)

name="ali"
age=5
if name =="ali" or name =="john" and age >=2:
    print("welcome John and Ali")
else:
    print("Goodbye John and Ali")

numn=int(input("enter the numerator"))
numd=int(input("enter the denominator"))
if numn % numd == 0:
    print(numn, "is divisible by", numd)
else:
    print(numn,"is not divisible by", numd)

mean1=20
wrong_number=18
correct_number=25
total_number=75
sum=mean1*total_number
print(sum)

num2=(sum-wrong_number)+correct_number
print("the corrected sum is",num2)

mean2=num2/total_number
print(mean2)

a=input("enter a number")
b=input("enter a number")
c=input("enter a number")
avg=(a+b+c)/3
if avg>a and avg>b and avg>c:
    print("greater than all values")
elif avg>a and avg>b or avg<c:
    print("greater than two values")
elif avg>a:
    print("greater than",a)
else:
    print("error")