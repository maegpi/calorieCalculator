#0.1
#maegpi
#initialized 2020-12-07
"""
-------------------------------------------------------------
Improvement Ideas
-------------------------------------------------------------

#convert file read to readline and add each line to dictionary
#make this a class, proper class methods
#pickle instead of dictionary?
#sorting algorithm to sort dictionary
#quit method to improve time-complexity of adding items

"""
BASE_GRAMS = 100
foodBank = open('foodBank.txt','r').read().split("\n")
if foodBank[-1] == "":
    foodBank.remove(foodBank[-1])

food_dict = {}
for food in foodBank:
    foods,calories = food.split(":")
    food_dict[foods] = int(calories)


def emptyBank():
    update = open('foodBank.txt','r+')
    update.truncate(0)
    update.close()
    return

def updateBank():
    emptyBank()
    with open('foodBank.txt','w') as writer:
        for item in food_dict:
            writer.write(item+":"+str(food_dict[item])+"\n")
    return
        
def addFood(food,calories,grams):
    if food_dict.get(food) is None:
        #Sets calories / 100g
        if grams != BASE_GRAMS:
            calories = int(((BASE_GRAMS * calories) / grams)+1)
        food_dict[food] = calories
        updateBank()
        return
    else:
        print(food,"is already in the dictionary!")
        return
    
def removeFood(food):
    if food_dict.get(food) is None:
        print(food,"is not in the dictionary!")
        return
    else:
        food_dict.pop(food)
        updateBank()
        return

def getCalories(food,grams):
    if food_dict[food] is None:
        return "Food not found!"
    else:
        baseCal = food_dict.get(food)
        return int(((grams * baseCal) / BASE_GRAMS)+1)

def updateFood(food,calories,grams):
    if grams != BASE_GRAMS:
        calories = int(((BASE_GRAMS * calories) / grams)+1)
    food_dict[food] = calories
    updateBank()
    return

def listMethods():
    return "addFood(food,calories,grams)\nupdateFood(food,calories,grams)\nremoveFood(food)\ngetCalories(food,grams)"

def printFoods():
    for item in food_dict:
        print(item,":",food_dict[item],"calories per",BASE_GRAMS,"grams")
    return

if __name__ == "__main__":

    checkEnd = False
    calorieCounter = 0
    currentCal = 0
    food = ""
    calorie = 0
    grams = 0
    while checkEnd is False:
        food = ""
        calorie = 0
        grams = 0
        currentCal = 0
        command = input("What would you like to do? Add, Update, Remove, Get, Print, Help, End: ")
        if command.upper() == "ADD":
            food,calorie,grams = input("Input Food Name, Calorie, Grams: ").split()
            addFood(food.upper(),int(calorie),int(grams))
            print(food.upper(),calorie,grams,"were added!")
        elif command.upper() == "UPDATE":
            food,calorie,grams = input("Input Food Name, Calorie, Grams: ").split()
            updateFood(food.upper(),int(calorie),int(grams))
            print(food,calorie,grams,"were updated!")
        elif command.upper() == "REMOVE":
            food = input("Input Food Name to remove: ")
            removeFood(food.upper())
            print(food,"was removed!")
        elif command.upper() == "GET":
            food,grams = input("Input Food Name and Grams: ").split()
            currentCal = getCalories(food.upper(),int(grams))
            calorieCounter += getCalories(food.upper(),int(grams))
            print(food,"contains",currentCal,"calories\nCurrent calorie count is: ",calorieCounter)
        elif command.upper() == "HELP":
            print(listMethods())
        elif command.upper() == "PRINT":
            printFoods()
        elif command.upper() == "END":
            print("Total calorie count is: ",calorieCounter)
            checkEnd = True
        else:
            print("Invalid input!")
