x=5
if (type(x) is int):
    print("true")
else:
    print("False")

x=5.5
if (type(x) is not float):
    print("true")
else:
    print("false")

x=20
y=20
if id(x) is id(y):
    print("x and y SAME identity")
    
y=30
if id(x) is not id(y):
    print("x and y have DIFFERENT identity")
