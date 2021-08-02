import random
# Present a menu to users that says the following:
# Hi my name is ___ 

# Enter "about" to learn more about me

# Enter "q&a" to ask me a question

# Enter "guestbook" to get added to my guestbook

# Enter "random" for something random

# Enter "goodbye" to say goodbye!

# Beginning menu MAINNNNN
# print(input("Hi my name is Ezekiel..." "\n" "Enter 'about' to learn more about me" "\n" "Enter 'q&a' to ask me a question" "\n" "Enter 'guestbook'"
# " to get added to my guestbook" "\n" "Enter 'random' for something random"  "\n" "Enter 'goodbye' to say goodbye!"))


# Where the user places thier choice
# input("Please enter here ")




# Enter "goodbye" to say goodbye!")


# about_me = ("My name is Ezekiel I'm a fun guy I like to make progress" "\n" 
# "uhmmm I mean you have to ask me more questions in order for me to tell you about myself I just give you a whole spill" "\n" 
# "I dont even know where your sitting at (Kawaki Leonards laugh)")

# def vlog ():
#     print(about_me)
#     return (vlog)   

# word = ""
# while():
#     word = print(input("Hi my name is Ezekiel..." "\n" "Enter 'about' to learn more about me" "\n" "Enter 'q&a' to ask me a question" "\n" "Enter 'guestbook'"
#     " to get added to my guestbook" "\n" "Enter 'random' for something random"  "\n" "Enter 'goodbye' to say goodbye!" "\n" "Please Type Here: "))
#     if word == about_me:
#         print(about_me)
                            
# print(about_me)

#     print(input("Hi my name is Ezekiel..." "\n" "Enter 'about' to learn more about me" "\n" "Enter 'q&a' to ask me a question" "\n" "Enter 'guestbook'"
# " to get added to my guestbook" "\n" "Enter 'random' for something random"  "\n" "Enter 'goodbye' to say goodbye!"))

# This is the about me page


# # def problems ():

# #     print("Welcome to the calulater menu!! ")

# #     number1 = int(input("What is the first number you want to divide?? " ))
# #     number2 = int(input("What is the second number you want to divide?? "))

# #     answer = (number1 / number2)
    
# #     return(answer)
# # print(problems())

# def about_me():
#     bio = print("\n" "Here's some information about me :)" "\n" "\n" "I am a nice guy, I like being nice and enjoy being around nice people",
#     "I am not confident in my knowledge in coding yet " "\n""I wish I could be a robot and just remember things easily""\n")
#     return(bio)
# about_me()

# def q_and_a(): 
#     random_answers = ["Answer1: Yes, I am 21...Oh did that not answer your question??" "\n","Answer2: I would like to visit New York...""\n",
#     "Answer3: Yes, my favorite fruit is Watermelon!!""\n"]
#     answer = random.choice(random_answers)
#     return(answer)
# print(q_and_a())

# wedding_registry  = {} # Dictionary name
    
# def guestbook():
#     first_name = (input("What is your first name?: " )) # asking the user for for thier first name 
#     last_name = (input("What is your last name?: ")) # asking the user for for thier last name 
#     message = (input("Would you like to leave your friend a message?: ")) # asking the user for for a messsage they want to give 
#     print(first_name + " " + last_name + " says "+ message) # prints the whole message they want to give the weddding couple 
#     wedding_registry = { first_name ,last_name, message } # inputs all the data into the dictionary 
#     print(wedding_registry) # To confirm it works I have added a print statement here
# guestbook() # Here i am calling the funcation idk it just doesn't work if I didn't call it


# study_topics = {}

# def random_topics ():
#     my_topics = ("loops", "bash file tree","functions", "lists")
#     users_study_topics = (input("what are some topics you have to work on?: "))
#     print("Woww same! Here are some of the topics I have to work on {} ".format(my_topics))
#     study_topics = my_topics, users_study_topics
#     print(" '\n' So together we have to sharpen our skills in {} ".format(study_topics))

# random_topics()
def about_me():
        bio = print("\n" "Here's some information about me :)" "\n" "\n" "I am a nice guy, I like being nice and enjoy being around nice people",
        "I am not confident in my knowledge in coding yet " "\n""I wish I could be a robot and just remember things easaboutily""\n")
        return(bio)
        
def q_and_a(): 
        random_answers = ["Answer1: Yes, I am 21...Oh did that not answer your question??" "\n","Answer2: I would like to visit New York...""\n",
        "Answer3: Yes, my favorite fruit is Watermelon!!""\n"]
        answer = random.choice(random_answers)
        return(answer)

def main ():
    user_word = (input("Hello My Name is Ezekiel Lewis" '\n' "Enter 'About' to learn more about me" "\n" "Enter 'Q&A' to ask me a question " "\n"
    "Enter 'Guestbook' to get added to my guestbook" "\n" "Enter 'Random' for something random" "\n" "Enter 'Goodbye' to say goodbye!: " "\n" ))
    print (user_word)
    if user_word == "About":
        print(about_me)
    elif user_word == "QA":
        print(q_and_a)
    else user_word == "goodbye":
        break
main() #How would I make it so once they choose an answer the whole program is not over?


