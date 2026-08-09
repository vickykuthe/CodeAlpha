from utils import (
    display_hangman,
    display_word,
    calculate_score
)


class HangmanGame:

    def __init__(self, word_data, difficulty):

        self.word = word_data["word"].lower()
        self.hint = word_data["hint"]

        self.difficulty = difficulty

        self.guessed_letters = set()

        self.wrong_guesses = 0
        self.hints_used = 0

        self.max_attempts = self.get_attempts()

    def get_attempts(self):

        difficulty_settings = {
            "easy": 8,
            "medium": 6,
            "hard": 4
        }

        return difficulty_settings.get(
            self.difficulty,
            6
        )

    def is_complete(self):

        return all(
            letter in self.guessed_letters
            for letter in self.word
        )

    def make_guess(self, letter):

        if letter in self.guessed_letters:
            return "duplicate"

        self.guessed_letters.add(letter)

        if letter in self.word:
            return "correct"

        self.wrong_guesses += 1

        return "wrong"

    def use_hint(self):

        if self.hints_used >= 1:
            return None

        self.hints_used += 1

        return self.hint

    def is_game_over(self):

        return (
            self.is_complete()
            or self.wrong_guesses >= self.max_attempts
        )

    def display(self):

        print("\n" + "=" * 50)

        display_hangman(self.wrong_guesses)

        print(
            "Word:",
            display_word(
                self.word,
                self.guessed_letters
            )
        )

        print(
            f"Wrong guesses: "
            f"{self.wrong_guesses}/"
            f"{self.max_attempts}"
        )

        print(
            "Guessed letters:",
            ", ".join(
                sorted(self.guessed_letters)
            )
        )

        print("=" * 50)

    def get_score(self):

        return calculate_score(
            self.word,
            self.wrong_guesses,
            self.hints_used
        )