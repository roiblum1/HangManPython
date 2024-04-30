"""
This function prints the hangman stages based on the number of tries.

Args:
num_of_tries (int): The number of tries the player has made.

Returns:
None: This function does not return any value. It only prints the hangman stages.
"""
def print_hangman(num_of_tries):
    stages = [
        "x-------x\n|       |\n|       0\n|      /|\\\n|      / \\\n|",    
        "x-------x\n|       |\n|       0\n|      /|\\\n|      /\n|",    
        "x-------x\n|       |\n|       0\n|      /|\\\n|\n|",            
        "x-------x\n|       |\n|       0\n|      /|\n|\n|",             
        "x-------x\n|       |\n|       0\n|       |\n|\n|",              
        "x-------x\n|       |\n|       0\n|\n|\n|",                      
        "x-------x\n|       |\n|\n|\n|\n|",                              
    ]

    if 0 <= num_of_tries < 7:
        print(stages[6 - num_of_tries])
    else:
        print("Invalid number of tries. Please enter a number between 0 and 6.")

"""
Check if the player has won the game based on the given secret word and the letters they have already guessed.

Args:
    secret_word (str): The secret word that the player is trying to guess.
    old_letters_guessed (List[str]): A list of letters that the player has already guessed.

Returns:
    bool: True if the player has won, False otherwise.
"""
def check_win(secret_word, old_letters_guessed):
    secret_word = secret_word.lower() 
    guessed_letters = set() 
    for guess in old_letters_guessed:
        if guess.lower() in secret_word:
            guessed_letters.add(guess.lower())
    return len(set(secret_word)) == len(guessed_letters)

"""
Function to display the secret word with guessed letters.

Args:
    secret_word (str): The secret word that the player is trying to guess.
    old_letters_guessed (List[str]): A list of letters that the player has already guessed.

Returns:
    None: This function does not return any value. It only prints the secret word with guessed letters.
"""
def show_hidden_word(secret_word, old_letters_guessed):
    word = list(secret_word)
    for c in word:
        if c in old_letters_guessed:
            print(c, end=" ")
        else:
            print("_", end=" ")
"""
Checks if the given letter is a valid input for the game.

Args:
    letter_guessed (str): The letter that the player has guessed.
    old_letters_guessed (List[str]): A list of letters that the player has already guessed.

Returns:
    bool: True if the letter is a valid input, False otherwise.

Raises:
    ValueError: If the letter is not a single alphabetic character.
"""
def check_valid_input(letter_guessed, old_letters_guessed):
    return letter_guessed.isalpha() and len(letter_guessed) == 1 and letter_guessed.lower() not in old_letters_guessed

"""
Checks if the given letter is a valid input for the game.

Args:
    letter_guessed (str): The letter that the player has guessed.
    old_letters_guessed (List[str]): A list of letters that the player has already guessed.

Returns:
    bool: True if the letter is a valid input, False otherwise.

Raises:
    ValueError: If the letter is not a single alphabetic character.

Updates the list of old_letters_guessed with the new letter if it's valid.
"""
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed.lower(), old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower()) 
        return True
    else:
        print("X")
        if old_letters_guessed:
            sorted_letters = sorted(old_letters_guessed)
            print(" -> ".join(sorted_letters)) 
        return False

"""
Chooses a secret word from a file based on the provided file path and word index.

Args:
    file_path (str): The path to the text file containing a list of words.
    index (int): The index of the word to be chosen as the secret word.

Returns:
    tuple: A tuple containing the total number of unique words in the file and the chosen secret word.

Raises:
    FileNotFoundError: If the specified file path does not exist.
"""
def choose_word(file_path, index):
    try:
        with open(file_path, "r") as file:
            words = file.read().split()
            if not words:
                print("The file is empty. Please enter a valid file path.")
                file_path = input("Please try enter file path: ")
                return choose_word(file_path, index)
            if (index <= 0):
                print("The word index is invalid. Please enter a valid word index.")
                word_index = int(input("Please try enter word index: "))
                return choose_word(file_path, word_index)
            unique_words = set(words)
            while (index > len(words)):
                index -= len(words)
            selected_word = words[index-1]
            return (len(unique_words), selected_word)
    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")
        file_path = input("Please try enter file path: ")
        return choose_word(file_path, index)

def main():
    file_path = input("Please enter file path: ")
    word_index = int(input("Please enter word index: "))
    old_letters_guessed = []
    num_of_tries = 0
    num_unique_words, secret_word = choose_word(file_path, word_index)
    while num_of_tries < 7:
        show_hidden_word(secret_word, old_letters_guessed)
        print("\n")
        print_hangman(num_of_tries)
        letter_guessed = input("\nPlease enter a letter: ")
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if (letter_guessed not in secret_word):
                num_of_tries += 1
        if(check_win(secret_word, old_letters_guessed)):
            print("\nYou win!")
            break
    print("\n The secret word is: ", secret_word)
    
if __name__ == "__main__":
    print(print_hangman(0))
    main()