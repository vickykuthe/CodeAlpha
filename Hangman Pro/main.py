from words import WordManager
from player import Player
from leaderboard import Leaderboard
from game import HangmanGame


def show_banner():

    print("""
╔══════════════════════════════════════════╗
║                                          ║
║          🎮 HANGMAN PRO 🎮              ║
║                                          ║
║       Interactive Word Challenge         ║
║                                          ║
╚══════════════════════════════════════════╝
""")


def choose_category(word_manager):

    categories = word_manager.get_categories()

    print("\n📚 Categories")

    for index, category in enumerate(categories, 1):

        print(
            f"{index}. {category.title()}"
        )

    while True:

        try:

            choice = int(
                input("\nSelect category: ")
            )

            if 1 <= choice <= len(categories):

                return categories[choice - 1]

            print("Invalid category.")

        except ValueError:

            print("Please enter a number.")


def choose_difficulty():

    print("""
🎯 Difficulty

1. Easy
2. Medium
3. Hard
""")

    while True:

        choice = input(
            "Choose difficulty: "
        ).strip()

        difficulties = {
            "1": "easy",
            "2": "medium",
            "3": "hard"
        }

        if choice in difficulties:

            return difficulties[choice]

        print("Invalid choice.")


def play_game(player, word_manager, leaderboard):

    category = choose_category(word_manager)

    difficulty = choose_difficulty()

    word_data = word_manager.get_random_word(
        category
    )

    game = HangmanGame(
        word_data,
        difficulty
    )

    print(
        f"\n🎮 Category: {category.title()}"
    )

    print(
        f"🔥 Difficulty: {difficulty.title()}"
    )

    while not game.is_game_over():

        game.display()

        print("\nOptions:")
        print("1. Guess a letter")
        print("2. Use hint")

        choice = input(
            "\nChoose option: "
        ).strip()

        if choice == "1":

            letter = input(
                "Enter a letter: "
            ).lower().strip()

            if len(letter) != 1 or not letter.isalpha():

                print(
                    "⚠️ Enter exactly one alphabetic letter."
                )

                continue

            result = game.make_guess(letter)

            if result == "correct":

                print("✅ Correct guess!")

            elif result == "wrong":

                print("❌ Wrong guess!")

            elif result == "duplicate":

                print(
                    "⚠️ You already guessed that letter."
                )

        elif choice == "2":

            hint = game.use_hint()

            if hint:

                print(
                    f"\n💡 Hint: {hint}"
                )

            else:

                print(
                    "⚠️ Hint already used."
                )

        else:

            print("Invalid option.")

    game.display()

    if game.is_complete():

        score = game.get_score()

        print("\n🎉 YOU WON!")

        print(
            f"🏆 Score: {score}"
        )

        player.add_win(score)

        leaderboard.add_score(
            player.name,
            score
        )

    else:

        print("\n💀 GAME OVER!")

        print(
            f"The correct word was: "
            f"{game.word}"
        )

        player.add_loss()


def main():

    show_banner()

    word_manager = WordManager()

    leaderboard = Leaderboard()

    name = input(
        "👤 Enter your name: "
    ).strip()

    if not name:

        name = "Player"

    player = Player(name)

    while True:

        print("""
╔════════════════════════════════════╗
║            MAIN MENU               ║
╠════════════════════════════════════╣
║ 1. 🎮 Play Game                    ║
║ 2. 🏆 Leaderboard                  ║
║ 3. 📊 My Statistics                ║
║ 4. 🚪 Exit                         ║
╚════════════════════════════════════╝
""")

        choice = input(
            "Select option: "
        ).strip()

        if choice == "1":

            play_game(
                player,
                word_manager,
                leaderboard
            )

        elif choice == "2":

            leaderboard.display()

        elif choice == "3":

            print("\n📊 PLAYER STATISTICS")

            print(
                f"Player: {player.name}"
            )

            print(
                f"Games Played: "
                f"{player.games_played}"
            )

            print(
                f"Games Won: "
                f"{player.games_won}"
            )

            print(
                f"Total Score: "
                f"{player.score}"
            )

            print(
                f"Win Rate: "
                f"{player.win_rate():.2f}%"
            )

        elif choice == "4":

            print(
                "\n👋 Thanks for playing Hangman Pro!"
            )

            break

        else:

            print(
                "⚠️ Invalid menu option."
            )


if __name__ == "__main__":
    main()