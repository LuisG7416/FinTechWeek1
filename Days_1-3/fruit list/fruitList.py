favFruits = ["Mango", "Avocado", "Pineapple", "Grapes", "Pomegranate"]

print(favFruits)

favFruits.append("Orange")

print(favFruits)

enisFav = favFruits[2]

print(enisFav)

#favFruits.pop(2)
#favFruits.remove("Pineapple")
favFruits[2] = "Banana"

for fruit in favFruits:
    print("I like " + fruit + ".")
    
for fruit in range(0,len(favFruits)):
    print("I like " + favFruits[fruit])

print(favFruits)
#Fresh, Price, Ripe, Rating, Name, Allergic? 
fruitCriteria = [True, 0.20, True, True, 100, "Banana", True]
fruitCriteria = {
    "isFresh":True, 
"costPerPound": 0.20, 
"isRipe":True, 
"inSeason":True, 
"howMuchLike":100, 
"whatIsIt":"Banana", 
"isAllergic":True
}

print(fruitCriteria)

print(fruitCriteria["isAllergic"])

fruitCriteria["specialFeature"] = "GMO"

print(fruitCriteria)


for key in fruitCriteria:
    print("The answer to " + str(key) + " is " + str(fruitCriteria[key]) + ".")
    
print(fruitCriteria["specialFeature"])