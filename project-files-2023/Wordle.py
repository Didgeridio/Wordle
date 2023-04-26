import random
MAX_TRIES = 6

def start_game():
    #Defines rules of the game for player
    print("Welcome to my Wordle game!")
    print("The goal is to guess the 5 letter word within 6 tries!")
    print("If you guess the correct letter in the correct spot it will display a 2.")
    print("If you guess the correct letter in the wrong spot it will display a 1.")
    print("If you guess the wrong letter in the wrong spot it will display a 0.")
    print("\nGood luck!\n")

def get_target_words():
    #retrieves and returns the target word in a stripped list
    target_words = list(open("target_words.txt"))
    target_word = random.choice(target_words)
    target_word = list(target_word.strip())
    return target_word

def play_again():
    #asks the player if they would like to play again and executed accordingly
    response = input("Would you like to play again? (Y/N) ").upper()
    response = response
    if response == "Y":
        print("\n")
    else:
        exit()

def produce_results():
    #Prints out the players guess in a list so they can se how close they were
    results = list()
    for i in range(len(player_guess)):
        if player_guess[i] == target_word[i]:
            results.append(2)
        elif player_guess[i] in target_word:
            results.append(1)
        else:
            results.append(0)
    print(results)
    print(f"You have guessed {count} time(s).")

while True:
    start_game()
    count = 0
    target_word = get_target_words()
    while count < MAX_TRIES:
        file = open("all_words.txt")
        all_words = file.read().strip().split()
        #all_words allows us to check if the player_guess is valid
        player_guess = input("Please make your guess: ").lower()
        if player_guess == "":
            continue
        if player_guess not in all_words:
            print("Please enter a valid word!")
            continue
        else:
            count = count + 1
            player_guess = list(player_guess)
            if player_guess == target_word:
                print("Congratulations you have won.")
                play_again()
                break
            else:
                produce_results()
    if count == MAX_TRIES:
        print("Sorry you have ran out of guesses, better luck next time!")
        play_again()
