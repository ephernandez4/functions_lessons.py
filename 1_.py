from determineEligibility import determineEligibility_toGraduate, listOfmovies
# #functions are ways to wrap your code
# #into reuseable units

# #define a function with def
# #only define the function once
# #when I pass in a parameter
# #i am passing in a placeholder
# #for future information
# def say_hello(name,age,address):
#     print(f"Hello! {name}")
#     print(f"How are you?{name}")
#     print(f"{name} are {age} years old")
#     print(f"{name} live in {address}")
# #call the funtion
# #pass in information called an argument
# say_hello(" Alice!", 22, " 123 Main St")
# say_hello(" Paul!", 34, " 456 Main St")
# say_hello(" Bob!", 56, " 789 Main St ")
# say_hello(" Altair!", 45, " 101 Main St")


determineEligibility_toGraduate("Alice",120, 2.0,800)
determineEligibility_toGraduate("Bob",119, 1.9,799)

listOfmovies("The Matrix", 10, "action")
listOfmovies("The Hangover", 5, "comedy")
listOfmovies("The Ring", 3, "horror")

#the return statement is 
#used to returm a value from a function

#return= statement used to end a function
#       and send a result back to the caller

def  add(x,y):
    z=x+y
    return z

def subtract(x,y):
    z=x-y
    return z

def multiply(x,y):
    z=x*y
    return z

def divide(x,y):
    z=x/y
    return z

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))