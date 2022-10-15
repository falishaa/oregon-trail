#Falisha

import random



#functions

#name: addDay
#purpose: changes global variable process for what happens in one day (food, date, etc.)
#input: action 
#return: day added
def addDay():
  global FOOD
  global HEALTH
  global DAY1
  global DAY2
  global CURMONTH
  global CURDAY
  #subtracts food
  if FOOD_CHG == 0: #if player is NOT resting/hunting, standard amt of food is taken
    FOOD -= 5
  if FOOD_CHG == 1: #if player is resting, take less food
    FOOD -= 4
  if FOOD_CHG == 2: #if player is hunting, use more food
    FOOD -= 6
  #change health
  if DAY1 == CURDAY or DAY2 == CURDAY:
    HEALTH -= 1
  #change month/day
  if CURMONTH in month31Days and CURDAY == 31:
    CURMONTH += 1
    CURDAY = 1
  elif CURDAY == 30:
    CURMONTH += 1
    CURDAY = 1
  else:
    CURDAY += 1





#name: updateDays
#purpose: calls addDay random number of times
#input: number of days
#return: amount of days passed
def updateDays(numDays):
  global FOOD_CHG
  while(numDays > 0):
    addDay()
    numDays -= 1
  FOOD_CHG = 0 #resets food change


##**Actions

#name: help
#purpose: list commands
#input: action
#return: printed commands
def help():
    print"[T]ravel: Travel a random amount of distance, takes 3 to 7 days"
    print"[R]est: Take the day to relax, restoring health a random amount for 2 to 5 days"
    print"[H]unt: Add 100lbs of food to inventory, takes 2 to 5 days"
    print"[S]tatus: Check health, food, distance traveled, and the current day"
    print"[C]Help: List commands"
    print"[Q]uit: Ends the game"
    print

#name: travel
#purpose: user travels certain amount of days, stats go down
#input:
#return: user has traveled
def travel():
  global REMDISTANCE
  global AMT_TRAVELED
  REMDISTANCE = REMDISTANCE - random.randint(30,60)
  AMT_TRAVELED = 2000 - REMDISTANCE
  updateDays(random.randint(3,7))
  if not AMT_TRAVELED >= 2000:
    print "You have traveled " + str(AMT_TRAVELED) + " miles."

#name: rest
#purpose: player stops traveling for set amount of days to restore health
#input: user action
#return:
def rest():
  global HEALTH
  global FOOD_CHG
  FOOD_CHG = 1
  if HEALTH < 5:
    HEALTH += 1
  updateDays(random.randint(2,5))
  print "You have finished resting."

#name: hunt
#purpose: adds random amount food
#input: user action
#return: new food amount
def hunt():
  global FOOD
  global FOOD_CHG
  FOOD_CHG = 2
  FOOD += 100
  if FOOD > 500:
    FOOD = 500
  updateDays(random.randint(2,5))
  print "You have gained 100 pounds of food."

#name: status
#purpose: prints current user stats including current day, health, miles traveled/left, and food left
#input: user presses "s"
#return: print statement with stats
def status():
  print"The date is " + str(CURMONTH) + "/" + str(CURDAY) + "."
  print "You currently have " + str(HEALTH) + " health and " + str(FOOD) + " pounds of food."
  print"You have traveled " + str(AMT_TRAVELED) + " miles, with " + str(REMDISTANCE) + " miles to go."
  




#main

#vars
REMDISTANCE = 2000
HEALTH = 5
FOOD = 500
AMT_TRAVELED = 0
death = False
CURDAY = 1
CURMONTH = 3
month31Days = [3, 5, 7, 8, 10, 12]
DAY1 = 4
DAY2 = 15
FOOD_CHG = 0



print"Welcome to Oregon Trail. Your goal is to travel from NYC to Oregon (2000 miles) by December 31st."
print"Be wary of your health and other stats. Use the status command to check."
print
print"Commands:"
print"[T]ravel: Travel a random amount of distance, takes 3 to 7 days"
print"[R]est: Take the day to relax, restoring health a random amount for 2 to 5 days"
print"[H]unt: Add 100lbs of food to inventory, takes 2 to 5 days"
print"[S]tatus: Check health, food, distance traveled, and the current day"
print"[C]Help: List commands"
print"[Q]uit: Ends the game"
print
name = input("What's your name, traveler?")

while death == False:
  action = input("What would you like to do today, " + name + "?")
  if action == "t": #run travel function
    travel()
    
  if action =="r": #run rest function
    rest()
    
  if action == "s": #run status function
    status()
  
  if action == "c": #help
    help()
    
  if action == "h": #hunt
    hunt()

  if action == "q": #quit
    death = True
  if FOOD <= 0:
    print"You have died of starvation."
    death = True
  if HEALTH <= 0:
    print"Your health has reached zero. You have died."
    death = True
  if REMDISTANCE <= 0:
    if AMT_TRAVELED >= 2000:
      print"YOU DID IT!!!"
      print"GG"
      death = True
  if CURMONTH == 13:
    if AMT_TRAVELED < 2000:
      print"You've run out of time..."
      death = True

#user has died or game has ended
print"Game over!"
