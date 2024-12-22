from colorama import Fore, Back, Style
import random

def guess_word():
    try:
        words = ["apple", "banana", "grape", "orange", "mango"]
        secure_random = random.SystemRandom()
        word = secure_random.choice(words)
        attempts = 6
        guessed_word = ["_"] * len(word)

        print(f"{Fore.RED}*** Welcome to the guess game ***{Fore.RESET}")
        print(f"{Fore.CYAN}You have {attempts} attempts.{Fore.RESET}")
        print(" ".join(guessed_word))
        
        while attempts > 0:
                guess = input(f"{Fore.YELLOW}Please guess the word: {Fore.RESET}").lower()

                if len(guess) != 1 or not guess.isalpha():
                    print(f"{Fore.RED}Please enter only a single letter!{Fore.RESET}\n")
                    continue

                if guess in guessed_word:
                    print(f"{Fore.YELLOW}You already guessed this letter!{Fore.RESET}\n")
                    continue
                
                if guess in word:
                    for i in range(len(word)):
                        if word[i] == guess:
                            guessed_word[i] = guess
                    print(f"{Back.LIGHTGREEN_EX}{Fore.BLACK}Well done, It's Correct!{Fore.RESET}{Back.RESET}")
                else:
                    attempts -= 1
                    print(f"{Back.RED}{Fore.BLACK}Wrong! remaining attempts {attempts}!{Fore.RESET}{Back.RESET}")
                
                for i in range(len(guessed_word)):
                    if guessed_word[i] == "_":
                        print(Fore.WHITE + guessed_word[i], end=" ")
                    else:
                        print(Fore.GREEN + guessed_word[i], end=" ")
                print(Style.RESET_ALL + "\n")

                if "_" not in guessed_word:
                    print(f"{Fore.GREEN}You win!, word: {word}{Fore.RESET}")
                    break
        else:
            print(f"{Fore.MAGENTA}You are run out of attempts, corret word: {word}{Fore.RESET}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print("An unxpected Error:", e)
