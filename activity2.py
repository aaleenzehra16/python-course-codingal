def find_cube(x):
    cube=x*x*x
    return cube
def divisible_by_three(y):
    if y%3 == 0:
        return find_cube(y)
    else:
        return False
print(divisible_by_three(21))
print(divisible_by_three(10))
