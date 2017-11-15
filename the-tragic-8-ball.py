import time
from random import randint
import sys

replies = ['Uh... maybe?', 'Go ask your mother.', 'Probably not.', 'With your luck?! Hahahahahahaha (breath) hahahahahahaha', 'What do you think?', 'I have to be honest, it doesn\'t look good.', 'How would I know that?', 'That kind of question has gotten you to where you are today.', 'Are you serious?']

def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.07)
    print()
    print()

def question():
    delay_print('What is your question?')
    question = input()
    print()
    delay_print('. . . . .')
    delay_print(replies[randint(0,8)])
    time.sleep(1)
    end()

def end():
    delay_print('Would you like to try again? (y/n)')
    user_reply = input()
    if user_reply == 'y':
        print()
        question()
    elif user_reply == 'n':
        print()
        delay_print('Later!')
        quit()
    else:
        delay_print('WRONG')
        end()

delay_print('I am the Tragic 8-Ball.')
time.sleep(1)
question()
