# import random
# import string

# chars = '' + string.punctuation + string.digits + string.ascii_letters
# chars = list(chars)
# key = chars.copy()

# random.shuffle(key)

# # print(f'chars{chars}')
# # print(f'key{key}')

# plain_text = input("Enter a massage to encrypt: ")
# cipher_text = ''

# for letter in plain_text:
#     index = chars.index(letter)
#     cipher_text += key[index]
    
# print(f"original massage: {plain_text}")
# print(f"encrpted massage: {cipher_text}")




# Hangman in python
# import random
# words = ['apple','banana','pineapple','orange']
# hangman_art = {0:("   ",
#                   "   ",
#                   "   "),
#                1:(" o ",
#                   "   ",
#                   "   "),
#                2:(" o ",
#                   " | ",
#                   "   "),
#                3:(" o ",
#                   "/| ",
#                   "   "),
#                4:(" o ",
#                   "/|\\ ",
#                   "   "),
#                5:(" o ",
#                   "/|\\",
#                   "/  "),
#                6:(" o ",
#                   "/|\\",
#                   "/ \\  ")
# }

# def display_man(wrong_guesses):
#     print("*********")
#     for line in hangman_art[wrong_guesses]:
#         print(line)
#     print("*********")

# def display_hint(hint):
#     print(' '.join(hint))

# def display_answer(answer):
#     print(' '.join(answer))

# def main():
#     answer = random.choice(words)
#     hint = ["_"] * len(answer)
#     wrong_guesses = 0
#     guesses_letter = set()
#     is_runinig = True
    
#     while is_runinig:
#         display_man(wrong_guesses)
#         display_hint(hint)
#         guess = input("Enter a letter: ").lower()
        
#         if len(guess) != 1 or not guess.isalpha():
#             print("Invalid input")
#             continue
#         if guess in guesses_letter:
#             print(f"[{guess}] already guessed")
#             continue
#         guesses_letter.add(guess)
        
#         if guess in answer:
#             for i in range(len(answer)):
#                 if answer[i] == guess:
#                     hint[i] = guess
                    
#         else:
#             wrong_guesses += 1
            
#         if '-' not in hint:
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print("YOU WIN!")
#             is_runinig = False
                        
#         elif wrong_guesses >= len(hangman_art) -1:
#             display_man(wrong_guesses) 
#             display_answer(answer)
#             print("YOU LOSS!")
#             is_runinig = False
            
        
    
# if __name__ == '__main__':
#     main()



import random

words = ['apple','banana','pineapple','orange']
hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" o ",
                  "   ",
                  "   "),
               2:(" o ",
                  " | ",
                  "   "),
               3:(" o ",
                  "/| ",
                  "   "),
               4:(" o ",
                  "/|\\ ",
                  "   "),
               5:(" o ",
                  "/|\\",
                  "/  "),
               6:(" o ",
                  "/|\\",
                  "/ \\  ")
}


def display_man(wrong_guess):
    for line in hangman_art[wrong_guess]:
        print(line)

def display_hint(hint, answer):
    print(' '.join(hint))

def display_answer(answer):
    print(' '.join(answer))

def main():
    answer = random.choice(words)
    hint = ['-'] * len(answer)
    wrong_guess = 0
    guess_letter = set()
    is_runing = True
    
    while is_runing:
        display_man(wrong_guess)
        display_hint(hint, answer)
        
        guess = input("Enter a letter: ")
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")
            continue
        
        if guess in guess_letter:
            print(f'{guess} already guessed')
            continue
            
        guess_letter.add(guess)
    
    
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
      
                    
                
        else:
            wrong_guess += 1

        if '-' not in guess_letter:
            display_man(wrong_guess)
            display_hint(hint, answer)
            print("YOU WIN!")
            is_runing = True
            
        elif  wrong_guess >= len(hangman_art) -1:
            display_man(wrong_guess)
            display_hint(hint, answer)
            print('YOU LOSS')
            is_runing = False
         
    
if __name__ == '__main__':
    main()