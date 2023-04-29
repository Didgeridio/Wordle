import random
MAX_TRIES = 6


def start_game():
#Defines rules of the game for player
    print("Welcome to my Wordle game!")
    print("The goal is to guess the 5 letter word within 6 tries!")
    print("If you guess the correct letter in the correct spot it will display a +.")
    print("If you guess the correct letter in the wrong spot it will display a ?.")
    print("If you guess the wrong letter in the wrong spot it will display a X.")
    print("\nGood luck!\n")


def get_target_words():
    #retrieves and returns the target word in a stripped list
    target_words = list(open("target_words.txt"))
    target_word = random.choice(target_words)
    return target_word


def play_again():
    #asks the player if they would like to play again and executed accordingly
    response = input("Would you like to play again? (Y/N) ").upper()
    response = response
    if response == "Y":
        print("\n")
    else:
        exit()


def remove_doubles(player_guess_list, target_word_list):
    for i in range(len(player_guess_list)):
        if player_guess_list[i] == target_word_list[i]:
            player_guess_list[i] = 3
            target_word_list[i] = 3


def produce_results():
    #Returns the results of the guess in a list
    results = list()
    for i in range(len(player_guess_list)):
        if player_guess_list[i] == 3:
            results.append(2)
        elif player_guess_list[i] in target_word_list:
            results.append(1)
        else:
            results.append(0)
    return results


def format_results(player_guess, results):
    #Formats the returned results into an easier to see format
    for char in player_guess:
        print(char.upper(), end=" ")
    print()
    for result in results:
        if result == 2:
            print("+", end=" ")
        elif result == 1:
            print("?", end=" ")
        else:
            print("X", end=" ")
    print()


def guesses_remaining(MAX_TRIES, count):
    MAX_TRIES = int(MAX_TRIES)
    count = int(count)
    if count == 5:
        print(f"You have " + str(MAX_TRIES - count) + " try left!")
    else:
        print(f"You have " + str(MAX_TRIES - count) + " tries left!")


def count_file_win(target_word, count):
    #Open the file and append the secret word, winning and amount of guess to win
    #Then tell them the average amount of guesses to win
    fhand = open("number_of_tries.txt", "a")
    fhand.write(f"w{count}{target_word}")


def count_file_loss(target_word, count):
    fhand = open("number_of_tries.txt", "a")
    fhand.write(f"l{count}{target_word}")


def average_wins():
    matches = 0
    wins = 0
    guesses = 0
    win_count = open("number_of_tries.txt")
    for line in win_count:
        matches = matches + 1
        if line[0] == "w":
            wins = wins + 1
        guesses = (guesses + int(line[1]))
    print(f"You have played {matches} time(s) and won {wins} time(s)! On average it takes you {guesses / matches} "
          f"guesses per match!")


while True:
    start_game()
    count = 0
    target_word = get_target_words()
    while count < MAX_TRIES:
        file = open("all_words.txt")
        all_words = file.read().strip().split()
        #all_words allows us to check if the player_guess is valid
        target_word_list = list(target_word.strip())
        player_guess = input("Please make your guess: ").lower()
        if player_guess == "":
            continue
        if player_guess not in all_words:
            print("Please enter a valid word!")
            continue
        else:
            count = count + 1
            player_guess_list = list(player_guess)
            if player_guess_list == target_word_list:
                print("Congratulations you have won.")
                count_file_win(target_word, count)
                average_wins()
                play_again()
                break
            else:
                remove_doubles(player_guess_list, target_word_list)
                results = produce_results()
                format_results(player_guess, results)
                guesses_remaining(MAX_TRIES, count)
    if count == MAX_TRIES:
        print("Sorry you have ran out of guesses, better luck next time!")
        print(f"The correct word was: {target_word.upper()}\n")
        count_file_loss(target_word, count)
        average_wins()
        play_again()
