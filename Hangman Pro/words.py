import json
import random


class WordManager:

    def __init__(self, filename="data/words.json"):
        self.filename = filename
        self.words = self.load_words()

    def load_words(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)

        except FileNotFoundError:
            print("❌ Word database not found.")
            return {}

        except json.JSONDecodeError:
            print("❌ Invalid word database.")
            return {}

    def get_categories(self):
        return list(self.words.keys())

    def get_random_word(self, category):

        if category not in self.words:
            return None

        return random.choice(self.words[category])