'''
Created on 21-Feb-2023

@author: ankon
1. change the number range from 1 to 1,00,000
2. Game should ask us to guess a number
3. Give a clue of the number is higher or lower than the guess
4. Inform the player if he won 
'''
from random import randint
start = 1
end = 1000
value=randint(start, end)
print("The computer shows a number between", start, "and", end)
guess= None

while guess!=value:
    text=input("Guess the number:")
    guess=int(text)
    
    if guess<value:
        print("Number is higher")
    elif guess>value:
        print("Number is lower")
print("Congratulations! You guessed the number. You won!")        

