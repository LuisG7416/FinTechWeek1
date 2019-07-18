# print("Hello World")
# print("What's up?")

# #Datatypes
# #anything between quotes is a string
# print("There is no mistake here.")

# #integers/numbers
# print(7)
# print(7 + 9)
# print(7+9)

# print(4-8) #-4
# print(3*3) #9
# print(25/5) #5
# print(25/6) #4.something
# print(4**2) #16

# print(23%4) #3

# #functions and methods
# name = "John Jacob Jingleheimer Schmidt"
# print(name)

# print("Hello" + str(4))
# print(int("4"))

# #inputs!
# firstName = input("What is your first name?\n")
# lastName = input("What is your last name?\n")
# age = input("How old are you?\n")
# firstName = firstName.title()
# lastName = lastName.title()
# age = int(age) + 3

# legal = "You are allowed to drink alcohol!"
# if(age > 21):
#     legal = "You are not allowed to drink alcohol!"
    
        
    

# print("Hello Mr." + firstName + " " + lastName + "!\n" + "You will be " + str(age) + " in 3 years!\n" + legal )

#Control Flow

# number = int(input("What's your favorite number?\n"))
# if number%2 == 0:
#     print("Your number is even!\n")
# else:
#     print("Your number is odd!\n")
# elif number == "":
#     int(input("Please type in a digit number!\n"))
    
    
    
    
    
    
#For Loops
favAnimal = "Dinosaur"
for i in range(0,len(favAnimal)):
    if i == 1:
        print("The " + str(i) + "st letter is " + favAnimal[i])
    elif i == 2:
        print("The " + str(i) + "nd letter is " + favAnimal[i])
    elif i == 3:
        print("The " + str(i) + "rd letter is " + favAnimal[i])
        
    else:
        print("The " + str(i) + "th letter is " + favAnimal[i])