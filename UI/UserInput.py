'''
Created on 18 Dec 2017

@author: tothi
'''
def user_input():
    '''
    Input: inputs from the keyboard
    Output: It returns the input
    Restriction: the input must be an integer!
    '''
    userInput = 0
    while True:
        try:
            userInput = int(input("Enter a value: "))       
        except ValueError:
            print("Not an integer!")
            continue
        else:
            return userInput
            break
def string_input():
    '''
    Input : we input a string
    '''
    return input('Enter the name: ')