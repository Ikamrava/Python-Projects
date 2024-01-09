import random
import art
HARD_LEVELE = 5
EASY_LEVEL = 10


def check_answer(guess, answer):
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVELE
  
def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1,100)
    turns = set_difficulty()
    
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns -= 1
        check_answer(guess, answer)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
game()



    


    
    






        
    
      
        
        
        
            
    
        
    
        
    







