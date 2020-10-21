"""This program is the design of the simple chatbot
1.The bot will starts asking the name of the person.
2.It welcomes the person with greetings and introduce itself.
3.Bot will ask the person want to do,it will offer a choice of things based up on the bot design.
4.It will respond to user to input correctly.  """


#imported required modules and files
from datetime import datetime
from greetings import welcome,self_intro
from month import months
from evaluator import evaluate

#Choice of things based on bot design
def show_menu():
    print("1.Events in a month")
    print("2.Calculate an expression")
    print("3.End this chat")
    print("---------------------------")
    #throws an exception if the choice is invalid
    try:
        return int(input("Enter your choice [1-3] "))
    except:
        return("Only enter the choice from 1 to 3")
        return 0

#chatbot performs the operations according to the person choice
def chatbot():
    #takes input from the user
    name=input("May I know your name please? ")
    #calling welcome function from greetings.py
    welcome(name)
    #calling show_menu function
    choice = show_menu()
    while choice !=3:
        #if choice is equal to 1 calls months function from month.py
        if choice == 1:
            months()
        #if choice is equal to 2 calls evaluate function from evaluator.py
        elif choice == 2:
            evaluate()
        #invalid choice
        else:
            print("Sorry, I don't understand that.")
        choice = show_menu()


#calls chatbot function
chatbot()