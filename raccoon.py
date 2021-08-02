# # import turtle
# # skk = turtle.Turtle()

# # for i in range (4):
# #     skk.forward(50)
# #     skk.right(90)
# #     skk.forward(50)
    
# # turtle.done()
# # turtle.done()


# import random
# def CollectStrings():
#    string_list = []
#    while True:
#       string = ("What is your question: (enter to quit): ")
#       if not string:
#          return string_list
#       string_list.append(string)

# def ChooseStrings(how_many):
#   string_list = CollectStrings()
#   chosen = random.sample(string_list, how_many)
#   chosen.sort()
#   return ', '.join(chosen)

# print (ChooseStrings (3))

import random

def q_and_a(): 
    random_answers = ("Answer1: Yes, I am 21...Oh did that not answer your question??" "\n","Answer2: I would like to visit New York...""\n",
    "Answer3: Yes, my favorite fruit is Watermelon!!""\n")
    answer = random.choice(random_answers)
    return(answer)

def about_me():
    bio = print("\n" "Here's some information about me :)" "\n" "\n" "I am a nice guy, I like being nice and enjoy being around nice people",
    "I am not confident in my knowledge in coding yet " "\n""I wish I could be a robot and just remember things easily""\n")
    return(bio)

def guestbook():
    first_name = (input("What is your first name?: " )) # asking the user for for thier first name 
    last_name = (input("What is your last name?: ")) # asking the user for for thier last name 
    message = (input("Would you like to leave your friend a message?: ")) # asking the user for for a messsage they want to give 
    print(first_name + " " + last_name + "Says "+ message) # prints the whole message they want to give the weddding couple 
    wedding_registry = { first_name ,last_name, message } # inputs all the data into the dictionary 
    print(wedding_registry) # To confirm it works I have added a print statement here
 # Here i am calling the funcation idk it just doesn't work if I didn't call it
# study_topics = {}

def random_topics ():
    my_topics = ("loops", "bash file tree","functions", "lists")
    users_study_topics = (input("what are some topics you have to work on?: "))
    print("Woww same! Here are some of the topics I have to work on {} ".format(my_topics))
    study_topics = my_topics, users_study_topics
    print("So together we have to sharpen our skills in {} ".format(study_topics))

#This block of code connects everything 
def main ():
   while user_word != "goodbye":
      user_word = (input("Hello My Name is Ezekiel Lewis" '\n' "Enter 'about' to learn more about me" "\n" "Enter 'Q&A' to ask me a question " "\n"
      "Enter 'Guestbook' to get added to my guestbook" "\n" "Enter 'Random' for something random" "\n" "Enter 'Goodbye' to say goodbye!: " "\n" ))
      print (user_word)
      # while user_word != "goodbye":
      if user_word == "about":
         print(about_me)
         about_me()
      elif user_word == "Q&A":
         print(q_and_a())
      elif user_word == "guestbook":
         print(guestbook)
         guestbook()
      elif user_word == "random":
         print(random_topics)
         random_topics()
   else: 
         print("Please type one of the words from the list.")
   user_word = input("Enter your choice again")
   print("Thank you for playing this game :)")
main()

