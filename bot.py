"""This program is the design of the simple chatbot
1.The bot will starts asking the name of the person.
2.It welcomes the person with greetings and introduce itself.
3.Bot will ask the person want to do,it will offer a choice of things based up on the bot design.
4.It will respond to user to input correctly.  """


import random
from datetime import datetime

def self_intro():
    responses =[
        "Its very good to see you.I am a chatbot.I can help to know an events in a particular month in 2020 and also do some calculations."
    ]
    return (random.choice(responses))

def time_greetings():
    current_time=datetime.now()
    greeting="Good Morning"
    if current_time.hour>12 and current_time.hour<=17:
        greeting="Good Afternoon"
    elif current_time.hour>17 and current_time.hour<=22:
        greeting="Good Evening"
    elif current_time.hour>22:
        greeting="Thats late"
    return greeting

def welcome(name):
    print(time_greetings(),name,self_intro())

def show_menu():
    print("1.Events in a month")
    print("2.Calculate an expression")
    print("3.End this chat")
    print("---------------------------")
    try:
        return int(input("Enter your choice [1-3] "))
    except:
        return("Only enter the choice from 1 to 3")
        return 0

def months():
        month_name=input("Enter a month name: ")
        if month_name=="January":
            print("The date,day and events days which are celebrated on January")
            print("-----Date: 1,Day: Wednesday,Event: New Year's Day-----")
            print("-----Date: 15,Day: Wednesday,Event: Makara Sankranti-----")
            print("-----Date: 26,Day: Sunday,Event: Republic Day-----")
            print("-----Date: 30,Day: Thursday,Event: Vasant Panchami-----")
        elif month_name=="February":
            print("The date,day and events which are celebrated on February")
            print("-----Date: 21,Day: Friday,Event: Maha Shivaratri-----")
        elif month_name == "March":
            print("The date,day and events which are celebrated on March")
            print("-----Date: 10,Day: Tuesday,Event: Holi-----")
        elif month_name == "April":
            print("The date,day and events which are celebrated on April")
            print("-----Date: 2,Day: Thursday,Event: Ramanavami-----")
            print("-----Date: 25,Day: Wednesday,Event: Ugadi-----")
            print("-----Date: 10,Day: Friday,Event: Good Friday-----")
        elif month_name == "May":
            print("The date,day and events which are celebrated on May")
            print("-----Date: 25,Day: Monday,Event: Ramzan-Eid-----")
        elif month_name == "June":
            print("The date,day and events which are celebrated on June")
            print("-----Date: 3,Day: Tuesday,Event: Rathayatri-----")
        elif month_name == "July":
            print("The date,day and events which are celebrated on July")
            print("-----No Events-----")
        elif month_name == "August":
            print("The date,day and events which are celebrated on August")
            print("-----Date: 3,Day: Monday,Event: Raksha Bandhan-----")
            print("-----Date: 11,Day: Tuesday,Event: Janmastami-----")
            print("-----Date: 15,Day: Saturday,Event: Independence day-----")
            print("-----Date: 22,Day: Saturday,Event: Vinayaka Chavathi-----")
            print("-----Date: 31,Day: Monday,Event: Onam-----")
        elif month_name == "September":
            print("The date,day and events which are celebrated on September")
            print("-----No Events-----")
        elif month_name == "October":
            print("The date,day and events which are celebrated on October")
            print("-----Date: 2,Day: Friday,Event: Mahatma Gandhi Jayanthi-----")
            print("-----Date: 25,Day: Sunday,Event: Dussehra-----")

        elif month_name == "November":
            print("The date,day and events which are celebrated on November")
            print("-----Date: 14,Day: Saturday,Event: Diwali-----")
        elif month_name == "December":
            print("The date,day and events which are celebrated on December")
            print("-----Date: 25,Day: Friday,Event: Christmas-----")
        else:
            print("Please check the month name")

def evaluate():
    expr=input("Enter an expression: ")
    try:
        print("Result of the given expression is: ",eval(expr))
    except Exception as e:
        print(e)


def chatbot():
    name=input("May I know your name please? ")
    welcome(name)
    choice = show_menu()
    while choice !=3:
        if choice == 1:
            months()
        elif choice == 2:
            evaluate()
        else:
            print("Sorry, I don't understand that.")
        choice = show_menu()

chatbot()