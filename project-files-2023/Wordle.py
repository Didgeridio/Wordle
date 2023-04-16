def get_target_words():
    import random
    target_words = list(open("target_words.txt"))
    target_word = random.choice(target_words)
    return(target_word)
x = True
while x == True:
    print("Welcome to my Wordle game!")
    print("The goal is to guess the 5 letter word within 6 tries!")
    print("If you guess the correct letter in the correct spot it will display a 2.")
    print("If you guess the correct letter in the wrong spot it will display a 1.")
    print("If you guess the wrong letter in the wrong spot it will display a 0.")
    print("\nGood luck!\n")
    count = 0
    target_word = (get_target_words())
    target_word = list(target_word.strip())
    while count < 6:
        file = open("all_words.txt")
        all_words = file.read().strip().split()
        try:
            player_guess = input("Please make your guess: ")
            player_guess = player_guess.lower()
            if player_guess == "":
                continue
            if player_guess not in all_words:
                print("Please enter a valid word!")
                continue
            else:
                count = count + 1
                player_guess = list(player_guess)
                if player_guess == target_word:
                    #Put in a winning function here with option to play again!
                    print("Congratulations you have won.")
                    response = input("Would you like to play again? (Y/N) ")
                    if response == "Y":
                        print("\n")
                        break
                    else:
                        x = False
                        break
                else:
                    results = list()
                    i = 0
                    while i < len(player_guess):
                        if player_guess[i] == target_word[i]:
                            results.append(2)
                            i = i + 1
                        elif player_guess[i] in target_word:
                            results.append(1)
                            i = i + 1
                        else:
                            results.append(0)
                            i = i + 1
                    print(results)
                    print(f"You have guessed {count} time(s).")
        except Exception as e:
            print(e)

    if count == 6:
        print("Sorry you have ran out of guesses, better luck next time!")
        response = input("Would you like to play again? (Y/N) ")
        if response == "N":
            print("\n")
            break
        else:
            print("\n")
