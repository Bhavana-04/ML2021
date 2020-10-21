#import required modules and files
import random
from datetime import datetime

def self_intro():
    #declares show list of responses
    responses =[
        "Its very good to see you.I am a chatbot.I can help to know an events in a particular month in 2020 and also do some calculations."
    ]
    #pick a response at random and return that
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
    #calls time_greetings and self_intro functions
    print(time_greetings(),name,self_intro())
