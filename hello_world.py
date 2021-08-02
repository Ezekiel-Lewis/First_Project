# Write a function that takes two number, divides them and return the value of the division
''' def num1 (num,num2):
    return(num / num2)  
answer = num1(25, 5)
print(answer) '''


'''print("Welcome To The Interactive Quiz!! ")

def quiz ():
    score = 0  
    question1 = input("Who is the famous straw hat pirate? ")
    if question1 == ("Luffy"):
        print("Correct")
        score += 1
    else: 
        print("Incorrect")


    question2 = input("What is the command for creating a directory in terminal? ")
    if question2 == ("mkdir"):
        print("You've created a folder!")
        score += 1
    else:
        print("Nope thats not it sorry...")


    question3 = input("What is the Data Type for decimals? ")
    if question3 == ("float"):
        print("Yes it is a float")
        score += 1
    else:
        print("incorrect")
    print(score)
quiz() '''


'''Problem 2 "Julio Cesar Chavez Mark VII is an interplanetary space boxer, 
who currently holds the championship belts for various weight categories on many different planets within our solar system. 
However, it is often difficult for him to recall what his "target weight" needs to be on earth in order to make the weight class
on other planets. 
Write a program to help him keep track of this.
It should ask him what his earth weight is, and to enter a number for the planet he wants to fight on. 
It should then compute his weight on the destination planet based on the table below:'''

'''print("Welcome to the Weight Class Calculator ! ")


earth_weight = input( " How much is your earth weight?: " )

def planets( Venus, Mars , Jupiter, Saturn ,Uranus , Neptune ):

 # goal_weight's value is the number (0, 6) 
   # if range(0,6)
   # for goal_weight in range(0, 6) :
       # print("What planet weight goal do you want to check?: {} " .format(goal_weight)) # Getting the users input on what number/planet they want
       # planet = goal_weight[planets] # Create the variable that adds both the number and the 
        # print("Goal weight: {} ".format(planet))
#planets() 

        #Plant_Checker '''

''' Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number 
and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz". 
Use a  for loop ***  num%3 == 0 num%5 == 0 '''

for numbers in range (1, 101):
    print (numbers)
    if numbers%3 == 0 and numbers%5 == 0:
        print("FizzBuzz")
    elif numbers%3 == 0:
        print("Fizz")
    elif numbers%5 == 0:
        print("Buzz")

for numbers in range (1, 101):
    answer = "" 
    if numbers %3 == 0:
        answer = answer + "Fizz"
    if numbers %5 == 0:
        answer = answer + "Buzz"
    if answer == "":

        print(numbers)
    else:   
        print(answer)
