def display_hangman(wrong_guesses):

    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,

        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,

        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,

        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,

        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,

        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,

        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]

    print(stages[wrong_guesses])


def display_word(word, guessed_letters):

    result = []

    for letter in word:

        if letter in guessed_letters:
            result.append(letter)

        else:
            result.append("_")

    return " ".join(result)


def calculate_score(word, wrong_guesses, hints_used):

    base_score = len(word) * 100

    penalty = wrong_guesses * 20

    hint_penalty = hints_used * 50

    score = base_score - penalty - hint_penalty

    return max(score, 0)