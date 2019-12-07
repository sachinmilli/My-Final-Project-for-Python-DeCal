#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import unittest
import time


def Magic8Ball():
# Set count to how many times user wants to do the magic 8ball
    count_str = input("You fool! Let me englighten you. How many things do you want to know? ")

# Testing if input is not a number
    while True:
        if count_str.isdigit():
            count = int(count_str)
            break
        else:
            count_str = input("Are you serious? Just enter a number... didn't think humans were this unintelligent.")

# Instruction if input is 0 or very high
    if count <= 0:
        print("Why did you even shake me then...")
        time.sleep(5)
    
    elif count > 10:
        print("\nYou're joking right? You want to ask that many questions?\nSheesh.. not sure a magic ball is enough to make you feel better.\n")
        

# Possible Replies for the Magic8Ball
    answers = ["It is certain.", "Without a doubt", "You may rely on it.",
               "Outlook good.", "Signs point to yes.", "Reply hazy try again.",
               "Ask again.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
               "Don\'t count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

# Main loop 
    while count > 0:
        question = input("Type your question: ")
        print('Give me a second...')
        time.sleep(2)
        dice = random.choice(answers)
        print("\n", dice, "\n")
        while dice == answers[5] or dice == answers[6] or dice == answers[9]:
            question = input()
            print('Give me a second...')
            time.sleep(2)
            dice = random.choice(answers)
            print("\n", dice, "\n")
            time.sleep(1)
        count = count - 1
    else:
        time.sleep(1)
        replay = input("\nAnything else you would like to know? [Y/N]")
        if replay == 'Y' or replay == 'y':
            Magic8Ball()
        elif replay == 'N' or replay == 'n':
            print('You have been enlightened.')
        
    









# In[ ]:


Magic8Ball()


# In[ ]:




