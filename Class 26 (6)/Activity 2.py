import time
import random

num = random.randint(1,51)
def intro():
    print('May I ask you for your name?')
    
    global name
    name = input()
    print(name, ', we are going to play a game\nI am thinking of a number between 1 and 50')
    
    if (num % 2 == 0):
        x = 'even'
    else:
        x = 'odd'
        
    print('This is an',x,'number')
    time.sleep(0.5)
    print('Go ahead! Guess!')
    
def pick():
    GuessTaken = 0
    
    while GuessTaken < 6:
        time.sleep(0.25)
        enter = input('Guess : ')
        
        try:
            guess = int(enter)  
            
            if guess <= 50 and guess >= 1:
                GuessTaken += 1
                
                if GuessTaken < 6:
                    if guess < num:
                        print('My number is larger than what you have guessed')
                    if guess > num:
                        print('My number is smaller than what you have guessed')
                    if guess != num:
                        time.sleep(0.5)
                        print('Try Again!')
                        
                    if guess == num:
                        break
                    
            if guess > 50 or guess < 1:
                print("Silly Goose! That number isn't in the range!")   
                time.sleep(0.25)
                print('Please enter a number that between 1 to 50')
                
        except:
            print("I don't think that ",enter,' is a number. Sorry!')
            
    if guess == num:
        GuessTaken = str(GuessTaken)
        print('Good job, ',name,' You guessed my number in ',GuessTaken,' guess!')
        
    if guess != num:
       print('Nope! The number I was thinking of was ',str(num)) 
       
playagain = 'Yes'

while playagain == 'Yes' or playagain == 'yes' or playagain == 'Y' or playagain == 'y':
    intro()
    pick()
    print('Do you want to play again?')
    playagain = input()