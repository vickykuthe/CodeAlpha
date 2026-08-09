import json
import os


class Leaderboard:

    def __init__(self, filename="data/leaderboard.json"):
        self.filename = filename
        self.scores = self.load_scores()

    def load_scores(self):

        if not os.path.exists(self.filename):
            return []

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)

        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def add_score(self, player_name, score):

        self.scores.append({
            "name": player_name,
            "score": score
        })

        self.scores.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        self.scores = self.scores[:10]

        self.save_scores()

    def save_scores(self):

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                self.scores,
                file,
                indent=4
            )

    def display(self):

        print("\n" + "=" * 40)
        print("🏆 LEADERBOARD")
        print("=" * 40)

        if not self.scores:
            print("No scores available yet.")
            return

        for index, player in enumerate(self.scores, start=1):

            print(
                f"{index}. "
                f"{player['name']} - "
                f"{player['score']} points"
            )