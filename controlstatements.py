temparature = int(input("Enter temparature: "))

if temparature > 25:
    print("It is too hot")
else:
    print("It is too cold")

#A python program that checks three numbers and returns the smallest number
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 < num2 and num1 < num3:
    print(num1,"is the smallest number")
elif num2 < num1 and num2 < num3:
    print(num2,"is the smallest number")
else:
    print(num3,"is the smallest number")


#A python programs that checks numbers to determine the largest number
x = int(input("Enter x: "))
y=int(input("Enter x: "))
z=int(input("Enter x: "))


if x>y and x>z:
    print(x,"is the largest number")
elif y>x and y>z:
    print(y,"is the largest number")
else:
    print(z,"is the largest number")