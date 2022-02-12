from random import randint, sample
from selectors import PollSelector
from english_words import english_words_alpha_set

english_words_list = list(english_words_alpha_set)

class hangman:
    pole = [
        [["|"],
        ["|"],
        ["|"],
        ["|"],
        ["|"],
        ["|"],
        ["|"],
        ["|"],
        ["|"]],
        [["/", "-", "-", "-", "-"],
        ["|"],
        ["|"],
        ["|"],
        ["|"],
        ["|"],
        ["|"],
        ["|"],
        ["|"]],
        [["/", "-", "-", "-", "-"],
        ["|", " ", " ", " ", "O"],
        ["|"],
        ["|"],
        ["|"],
        ["|"],
        ["|"],
        ["|"],
        ["|"]],
        [["/", "-", "-", "-", "-"],
        ["|", " ", " ", " ", "O"],
        ["|", " ", " ", "", "/|\ "],
        ["|"],
        ["|"],
        ["|"],
        ["|"],
        ["|"],
        ["|"]],
        [["/", "-", "-", "-", "-"],
        ["|", " ", " ", " ", "O"],
        ["|", " ", " ", "", "/|\ "],
        ["|", " ", " ", " ", "|"],
        ["|"],
        ["|"],
        ["|"],
        ["|"],
        ["|"]],
        [["/", "-", "-", "-", "-"],
        ["|", " ", " ", " ", "O"],
        ["|", " ", " ", "", "/|\ "],
        ["|", " ", " ", " ", "|"],
        ["|", " ", " ", "", "/ \ "],
        ["|"],
        ["|"],
        ["|"],
        ["|"]],
        [["/", "-", "-", "-", "-"],
        ["|", " ", " ", " ", "O"],
        ["|", " ", " ", "", "/|\ "],
        ["|", " ", " ", " ", "|"],
        ["|", " ", " ", "", "/ \ "],
        ["|"],
        ["|"],
        ["|"],
        ["|", " ", "-/", "\-_", "\_",]],
        [["/", "-", "-", "-", "-"],
        ["|", " ", " ", " ", "O"],
        ["|", " ", " ", "", "/|\ "],
        ["|", " ", " ", " ", "|"],
        ["|", " ", " ", "", "/ \ "],
        ["|"],
        ["|", " ", " ", " ", " ", " ", " ", "`\ "],
        ["|"],
        ["|", " ", "-/", "\-_", "\_",]],
        [["/", "-", "-", "-", "-"],
        ["|", " ", " ", " ", "O"],
        ["|", " ", " ", "", "/|\ "],
        ["|", " ", " ", " ", "|"],
        ["|", " ", " ", "", "/ \ "],
        ["|"],
        ["|"],
        ["|", " ", "Ψ ", "Ψ ", "Ψ ",],
        ["|", " ", "-/", "\-_", "\_",]]
    ]

    def __init__(self, lives):
        self.stage = 8 - lives
    
    def display_hangman(self, pole):
        for i in pole:
           print("".join(i))

    def draw_hangman(self):
        self.display_hangman(self.pole[self.stage])

def add_space(answer):
    for i in range(len(answer)):
        answer[i] += " "
    return str("\n" + "".join(answer) + "Lives:")
def sub_space(answer):
    for i in range(len(answer)):
        answer[i] = answer[i][0]
    return str("\n" + "".join(answer) + "Lives:")

def game_logic(guess, word):
    result = []
    word = list(word)
    if guess in word:
        for i in range(len(word)):
            if guess == word[i]:
                result.append(i)
        return result
    else:
        return None

def replace(index_list, answer_list, word):
    for i in index_list:
        answer_list[i] = word[i]
    return answer_list

def game():
    word = str(english_words_list[randint(0, 25473)]).upper() #25474 is the length of the set
    answer = list(word[0]) + ["_"] * (len(word) - 1)
    letters_chosen = []
    letters = game_logic(word[0], word)
    answer = replace(letters, answer, word)
    letters_chosen.append(word[0])
    lives = 8
    while lives > 0 and list(word) != answer:
        
        hangman(lives).draw_hangman()
        print(add_space(answer), lives)
        sub_space(answer), lives
        guess = input("Enter a letter: ").upper()
        if guess.isalpha() and len(guess) == 1:
            if not guess in letters_chosen:
                letters = game_logic(guess, word)
                if letters == None:
                    lives -= 1
                else:
                    answer = replace(letters, answer, word)
                letters_chosen.append(guess)

    if lives == 0:
        hangman(lives).draw_hangman()
        print("YOU LOST! " + "The word was:", word)
    else:
        print(add_space(answer), lives)
        print("WINNER!", "lives:", lives)

def play():
    play_again = True
    while play_again:
        game()
        again = input("Do you want to play again? Y/N: ")
        if again.lower() != "y":
            play_again = False      

play()