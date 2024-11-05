#Built-in Functions

y=max(34,56, 70,18)
print(y)

x = min(40,67,34,25)
print(x)

z = pow(2, 3)
print("The result is",z)

#User-defined functions
def greeting():
    print("Hello there!")

greeting() #Calling Function

def multiply():
    a = 12
    b = 10
    print(a * b)

multiply()

#Parameters/Variable and Argument/Value
def add(x , y):
    print(x + y)

add(4,5)
add(60, 70)

def employee(fullname,age,position,status):
    print(fullname,age,position,status)

employee("Mark Joe",54,"CEO", "Married")
employee("Jane Ann",23,"HR", "Single")
employee("Job Harry",38,"Clerk", "Married")
employee("Mary Mbotela",25,"Receptionist", "Single")