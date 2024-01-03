import random
import hangman_art
import hangman_words


print("Welcome to the Hangman!")
print(hangman_art.logo)
word = random.choice(hangman_words.word_list)
print("I am thinking of a word that is",len(word),"letters long.")
print(word)
display = []
for i in range(len(word)):
    display.append("_") 


end_of_game = False
lives = 6

while not end_of_game:
    guessed_letter = input("Guess a letter: ").lower()
    for i in range(len(word)):
        if word[i] == guessed_letter:
            display[i] = guessed_letter
        
    if guessed_letter not in word:
      print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("You lose.")
        
    print(f"{' '.join(display)}") 

    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    print(hangman_art.stages[lives])
        
    
                

