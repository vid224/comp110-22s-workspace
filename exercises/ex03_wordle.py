"""EX03 - Wordle."""

__author__ = "730394746"


def contains_char(secret_word: str, search_character: str) -> bool:
    """Searches for search character in secret word."""
    assert len(search_character) == 1
    checking_index = 0
    while checking_index < len(secret_word):
        if search_character == secret_word[checking_index]:
            return True
        else:
            checking_index += 1
    return False


def emojified(guess_word: str, secret_word: str) -> str:
# Codes for assigning emojis to guesses
    """Assigns emojis to each character based on correctness."""
    assert len(guess_word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    checking_index = 0
    emoji: str = ""
    while checking_index < len(secret_word):
        if guess_word[checking_index] == secret_word[checking_index]:
            emoji += GREEN_BOX
        else:
            if contains_char(secret_word, guess_word[checking_index]):
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        checking_index += 1
    return emoji


def input_guess(num_of_chars: int) -> str:
# Codes to limit guess character length
    """Allow for the entry of guess word that is expected length."""
    guess: str = input(f"Enter a {num_of_chars} character word: ")
    while len(guess) != num_of_chars:
        guess = input(f"That wasn't {num_of_chars} chars! Try again: ")
    return guess


def main() -> None:
# Combines previous functions to work together to create a structured wordled
    """The entrypoint of the program and main game loop."""
    secret_word = "codes"
    turn = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if secret_word == guess:
            return print(f"You won in {turn}/6 turns!")
        else:
            turn += 1
    return print("X/6 - Sorry. try again tomorrow!")
    
    
if __name__ == "__main__":  # Allows for program to run as a module and import into other modules 
    main()    