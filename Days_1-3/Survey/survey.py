# firstName = input("What is your first name?\n")
# lastName = input("What is your last name?\n")
# age = input("How old are you?\n")
# firstName = firstName.title()
# lastName = lastName.title()
# age = int(age) + 3

# legal = "You are not allowed to vote!\n"
# if(age > 18):
#     legal = "You are allowed to vote!\n"

# vowel = "You do not have a vowel in your name!"

# if set('aeiou').intersection(firstName.lower()):
#     vowel = "You have a vowel in your name!"

# print("Hello " + firstName + " " + lastName + "! " + legal + vowel)

import random

dieOne = random.randint(0,6)
dieTwo = random.randint(0,6)

count = 1
while dieOne != 1 & dieTwo != 1:
    dieOne = random.randint(0,6)
    dieTwo = random.randint(0,6)
    count = count + 1
    
print(str(count))
