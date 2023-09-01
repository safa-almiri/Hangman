
import random


hangman_stages = [
    """
       ______
      |     |
      |     
      |    
      |     
      |    
    """,
    """
       ______
      |     |
      |     O
      |    
      |     
      |    
    """,
    """
       ______
      |     |
      |     O
      |     |
      |     
      |    
    """,
    """
       ______
      |     |
      |     O
      |    /|
      |     
      |    
    """,
    """
       ______
      |     |
      |     O
      |    /|\\
      |     
      |    
    """,
    """
       ______
      |     |
      |     O
      |    /|\\
      |    / 
      |    
    """,
    """
       ______
      |     |
      |     O
      |    /|\\
      |    / \\
      |    
    """
]



class Hangman:
    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        self.remaining_guesses = 6

    def guess(self, letter):
        if letter in self.word:
            self.guessed_letters.append(letter)
            return True
        else:
            self.remaining_guesses -= 1
            return False

    def display_word(self):
        displayed_word = " "
        for char in self.word:
            if char in self.guessed_letters:
                displayed_word += char + " "
            else:
                displayed_word += "_ "
        return displayed_word

  
    def is_game_over(self):
      if self.remaining_guesses == 0 or len(self.guessed_letters) == len(hangman_stages):
        return True
      elif set(self.word) == set(self.guessed_letters):
        return True
      else:
        return False



# List of words to choose from
words = ["python", "programming", "hangman", "computer", "game"]

# Randomly choose a word from the list
chosen_word = random.choice(words)

# Create an instance of Hangman class
game = Hangman(chosen_word)


print("Guess the word: ", game.display_word())

while not game.is_game_over():
    guess_letter = input("Enter a letter: ")
    if game.guess(guess_letter):
        print("Correct guess!")
    else:
        print("Wrong guess!")
      
        print(hangman_stages[len(game.guessed_letters)])
        print("Word: ", game.display_word())
        print("Remaining guesses: ", game.remaining_guesses)
   
if set(game.word) == set(game.guessed_letters):
    print("Congratulations! You won!")
else:
    print("Game over! You lost. The word was:", game.word)


