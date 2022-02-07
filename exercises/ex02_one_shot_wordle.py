"""EX02 - One Shot Wordle."""

__author__ = "730394746"

secret_word = "python"

guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
no_matching_character = True
# No matching character variable checks to see if the word includes the character in the checking index of interest. When there is no match throughout the word, variable becomes true and a white box will be added. If variable is false a yellow box is added. 
checking_index = 0
alt_checking_index = 0
emoji = ""

while checking_index < len(secret_word):
    if guess[checking_index] == secret_word[checking_index]:
        emoji += GREEN_BOX
        # The program first checks to see if the characters in the same index on both words match and if true, will add a green emoji and move to the next letter
    else:
        while no_matching_character and alt_checking_index < len(secret_word):  # These conditions allow the program to only look for matching characters throughout the word as long as the character has not been previously found in an earlier index in the guess word and the checking index is not greater than the length of the guess word
            if guess[checking_index] != secret_word[alt_checking_index]:
                alt_checking_index += 1
            else:
                emoji += YELLOW_BOX
                alt_checking_index += 1
                no_matching_character = False
                # Making the no matching character false allows for the program to move on to the next character without adding another white box
        if no_matching_character:
            emoji += WHITE_BOX
    alt_checking_index = 0
    checking_index += 1
    no_matching_character = True

print(emoji)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")