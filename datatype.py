
number = 56 #Integer
second = 43.12 #Float
greeting = "Hello there" #String
isPythonInteresting = True #Boolean

#Data Structures- Multiple values stored in a single variable
cars = ["toyota", "nissan", "vw"] #List - Ordered and changeable
fruits = ("banana","orange","apple") #Tupple - Ordered but unchangeable
countries = {"Kenya","Tunisia","Algeria"} #Set - Unordered but unchangeable
student = {
    "firstname" : "Michelle",
    "age" : 23,
    "course" : "Web Development",
    "nationality" : "Kenyan"
} #Dictionary - Key-value pair


print(cars)
print(fruits)
print(countries)
print(student)
print(student["firstname"])

print(number)
print(second)
print(isPythonInteresting)
print(greeting)



#Determining a datatype
print(type(student))
print(type(countries))

#Typecasting - Converting one data type into another
print(float(number))
print(int(second))

