def addition(a,b):
    return a+b

def subtract(a,b):
    return abs(a-b)
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))

print("x+y = ", addition(x,y))
print("x+y = ", subtract(x,y))