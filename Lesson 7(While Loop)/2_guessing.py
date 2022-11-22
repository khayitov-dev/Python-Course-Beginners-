### Guessing Game

secret_key = "Javokhir"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_key and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Taxminiy so'z yozing: ")
        guess_count += 1 
    else:
        out_of_guesses = True
        
if out_of_guesses:
    print("Taxminlaringiz barchasi xato, Siz yutkazdingiz!")
else:
    print("Siz yutdingiz!")