# # # '''team = ["Jabari", "Ezekiel", "Daizaria", "Kyle", "Jocelyn"]

# # # print(team[0])
# # # print(team[1])
# # # print(team[2])
# # # print(team[3])
# # # print(team[4])

# # # # how to make the team generator random
# # # print(team[random.randrange()]) '''

# # # # Write a Python function to find the Max of three numbers

# # # '''numbers = [2, 4, 6, 9, 17, 38] '''

# # # '''for ie in range (0, len(numbers)):
# # #     print (numbers[ie])
# # #     if (numbers[ie]%2==0 ):'''

# # # '''for num in numbers:
# # #     if(num%2== 0):
# # #         print (num) '''

# # # # Note : A prime number (or a prime) is a natural number greater than 1 and
# # # # that has no positive divisors other than 1 and itself.
# # # # Use %i to check if any number between 1 and number gives you a zero.

# # # # Write a Python function to find the Min of three numbers

# # # '''def min(num1, num2, num3):
# # #     if num1 <= num2 and num1 <= num3:
# # #         print("smallest number {} ".format(num1))
# # #     elif num2 <= num1 and num2 <= num3:
# # #         print ("smallest number {} ".format(num2))
# # #     else:
# # #         print("smallest number {} ".format(num3))

# # # min(1, 3, 2) '''
# # # # Write a Python function that accepts a string and calculates the number of uppercase letters and lowercase letters.


# # # '''def letters(word):
# # #     upper = 0
# # #     lower = 0 '''

# # # # Makes l = to a character
# # # #     for char in word :
# # # #         print (char)
# # # #         if char.isupper():
# # # #             upper+=1
# # # #         else:
# # # #             lower+=1
# # # #     print("upper{}".format(upper))
# # # #     print("lower{} ".format(lower))
# # # # letters("moon")

# # # # Write a Python function that takes a list of words
# # # # and return the longest word and
# # # # the length of the longest one

# # # # def Big_Words (words):
# # # #     word = ("") # Will use this word to keep track of the variable
# # # #     for a in words:
# # # #         print(a)
# # # #         if len(a) > len(word):
# # # #         word = a
# # # # Big_Words(["John", "Jacob" , "Jingle"])


# # # # #Data Structures:
# # # # Python Dictonary: is associative array (list). it contains a list of pairs of key-values. You can retrieve
# # # # values using specific keys.

# # # # #initalize dict
# # # # my_dict = {} #always use squggly braces

# # # # # initialize a dict with values
# # # # my_dict = {1: 'apple', 2:'ball'}

# # # # #Output: apple
# # # # print(my_dict['1'])

# # # # Ex.
# # # #     ex_dict = {"bob":"dylan", "hello":"world","jimmy":"neutron" }

# # # #     print(ex_dict["bob"])
# # # #     print(ex_dict["hello"])
# # # #     print(ex_dict["jimmy"])

# # # # Real_World_example:
# # # #     ex_dict = {"name": "John Doe", "address": "Elm street", "phone number": 212555555, "age":45,"pets":[ "kitty","fish","dog"] }
# # # #     print(ex_dict["name"])
# # # #     print(ex_dict["address"])
# # # #     print(ex_dict["phone number"])
# # # #     print(ex_dict["pets"])''
# # # '''fav_anime_chars ={"animes": ["Naruto", "OnePiece", "One Punch Man",
# # #     "Boruto", "Grand Blue", "Attack On Titan"],

# # # "best_characters": ["Naruto", "Zoro", "Garau", "Susake", "Eren Yeager"]
# # # }
 
# # # best_characters = {"Naruto": ["naruto", "sasuke"], "Zoro":"", "Garau":"", "Susake":"", "Eren Yeager":""}


# # # print(best_characters) '''

# # # # #Dictionary ex. 
# # # # #Print only the values
# # # # ex_dict = {"bob":"dylan","hello":"world","jimmy":"neutron" }
# # # # print(ex_dict.values()) prints dylan, world, and neutron
# # # # print(ex_dict.keys()) bob, hello, jimmy
# # # # print(ex_dict.items) bob:dylan, hello:world, jimmy:neutron


# # # # angels_class = {"Ezekiel":"Lewis", "Daizaria":"Randle", "Jabari":"Flowers","Jocelyn":"Diaz","Kyle":"Riley"}

# # # # for raccoon in angels_class.keys():
# # # #     print(raccoon)


# # # #Write a Python function to multiply all the values in a dict

# # # coffee = {'lattee':9.99,'Black_Coffee':5.99,'Ice_Coffee':2.99} #This is my libaray 
# # # result = 1 # I don't understand why they have the result here 
# # # for drink in coffee:    
# # #     result=result * coffee[drink] # result equals 1 so why does it cause it to muilply against itself??
# # # print(result)
# # # result = format(result, ".2f") # editing result
# # # print("All the coffee cost {} ".format(result))


# # # Movies = {'Spiderman_3': 7, 'Flowers_in_the_attic':8, 'Lean on me': 7.5, 'Grown_Ups': 6,}
# # # result = 1 
# # # for Top_4 in Movies:
# # #     print(Top_4)
# # #     result = result * Movies[Top_4]
# # # print(result)

# # # # print("Total rating of all movies listed is {} " .format(result))

# # # # Write a Python program to sum all the values in a dictionary.

# # # nums = {"computers":2, "book":6, "desktops":8, "tv":10, "alarms":12}
# # # answer = 0

# # # for ran in nums:
# # #     print(ran)
# # #     answer = answer + nums[ran]
# # # print(answer)


# # # Create a python script that takes a list of letter grades and counts the amount of each letter grade with a Dict
# #     # from typing import Counter


# # # from typing import Counter


# # # def gradCount():
# # #     grades = {'kyle': 'C', 'Jocelyn': 'A', 'Ezekiel': 'B'}
# # #     count = {}

# # #     for grade in grades.values():
# # #         print(grade)
# # #         if grade in grades:
# # #             grades
# # #         print(Count)
# # # gradCount()


# # def gradeList():
# #     grades=['A','B','A','C','C','C','D']
# #     CountA = 0
# #     CountB = 0
# #     CountC = 0 
# #     CountD = 0

# #     for letter in grades:
# #         if letter == 'A':
# #             CountA += 1
# #         if letter == 'B':
# #             CountB += 1
# #         if letter == 'C':
# #             CountC += 1
# #         if letter == 'D':
# #             CountD += 1
# #         if letter == 'E':
# #             CountE += 1

# #     print("Total As: {} ".format(CountA))
# #     print("Total As: {} ".format(CountB))
# #     print("Total As: {} ".format(CountC))
# #     print("Total As: {} ".format(CountD))

# # gradeList()


# # def gradDict():
# #     letters = ['A','B','C','D','E']
# #     count = {}

# #     for letter in letters:
# #         print(letter)
# #         if letter in count: 
# #             count[letter] += 1
# #         else:
# #             count[letter] = 1
        
# #     print(count)

# # gradDict()

# # exDict = {'A': 22}
# # print('A'in exDict)




# # # #gradlist()
# # # letters = ['A','B','C','D','E']

# # # def gradDict(letters):

# # #     count = {}
# # #     for letter in letters:
# # #         print(letter)
# # #         if letter in count:# if letter exists as a key 
# # #             count[letter] += 1 #adding 1 to key that already exist 
# # #         else:
# # #             count[letter] # key is added since value is assigned 

# # #     print(count)


# # # gradDict (['A','B','C','D','E'])

# # # exDict = {'A': 22}
# # # print ('A' in exDict)
# # # print('B' in exDict)

# # # exDict['B'] = 1
# # # print(exDict)

# # # Write a Python program to find the key of the maximum value in a dictionary


# # numbers = {"sam":160, "tom": 135, "rem":154, "harry": 350}

# # def weight(x):

# #     count = 0 
# #     key = "" #empty string

# #     for name in x: 
# #         print(name)

# # weight(numbers)

def problems ():

    print("Welcome to the calulater menu!! ")

    number1 = int(input("What is the first number you want to divide?? " ))
    number2 = int(input("What is the second number you want to divide?? "))

    answer = (number1 / number2)
    
    return(answer)

print(problems())















# # test1 = input("What did you get for test 1?")
# # test2 = input("What did you get for test 2?")
# # test3 = input("What did you get for test 3?")
# # average = (test1+test2+test3)/3
# # print(average)

# def world_problems ():
#     print ("How do we fix world problems?? ")

    




# def numbers():  #function definifion for subtraction
#     num1=int(input("Enter first number: "))
#     num2=int(input("Enter second number: "))
#     sub = num1 - num2
#     return sub
# def about():
#     bio = print(str("Here is some information about me" "\n" "I am a nice guy I like being nice and enjoy being around nice people"))
#     return(bio)

# def multi():
    
#     question1 = int(input("Pick a number "))
#     question2 = int(input("Pick another number"))
#     solution = (question1 * question2)
    
#     return(solution)


    
# def problems ():

#     print("Welcome to the calulater menu!! ")

#     number1 = int(input("What is the first number you want to divide?? " ))
#     number2 = int(input("What is the second number you want to divide?? "))

#     answer = (number1 / number2)
    
#     return(answer)

# def addNums():
#     print("You've chosen to perform addition! Prepare to enter two integers to add together...")
    
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
    
#     sum = num1 + num2
    
#     return sum

    
# def exp(num1,num2):
#     return num1 ** num2 
    
# def inc():

#     num1= int(input("give me one number")) # take user inputs and run the expo function i created for it

#     num2= int(input("give me another number"))
#     answer = exp(num1,num2)
#     return answer


# number = 1
# while(number != 6 ):
#     try:
#         number = int(input("Pick one: 1:add, 2:subtract, 3:divide, 4:multiply and 5:exponents 6:quit"))
#         if number == 1:
#             print(addNums())
#         elif number == 2:
#             print(numbers())
#         elif number == 3:
#             print(problems())
#         elif number == 4:
#             print(multi())
#         elif number == 5:
#             print(inc())
#         elif number == 6:
#             break
#         else:
#             print("Please type in a number from 1-6")
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
    

else = goodbye 



