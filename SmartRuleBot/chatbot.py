import json
import random
import re
from datetime import datetime

from database import save_message
from config import CONFIDENCE_THRESHOLD


class SmartRuleBot:

    def __init__(self):
        self.intents = self.load_intents()
        self.user_name = None

    # Load chatbot intents from JSON
    def load_intents(self):
        with open("data/intents.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        return data["intents"]

    # Clean and normalize user input
    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
        return text.strip()

    # Calculate similarity score between input and pattern
    def calculate_score(self, user_input, pattern):

        user_words = set(
            self.clean_text(user_input).split()
        )

        pattern_words = set(
            self.clean_text(pattern).split()
        )

        if not pattern_words:
            return 0

        # Find common words
        matched_words = user_words.intersection(pattern_words)

        score = len(matched_words) / len(pattern_words)

        # Give extra importance to exact phrase matching
        cleaned_input = self.clean_text(user_input)
        cleaned_pattern = self.clean_text(pattern)

        if cleaned_pattern in cleaned_input:
            score += 0.5

        return min(score, 1.0)

    # Find the best matching intent
    def find_intent(self, user_input):

        best_intent = None
        best_score = 0

        for intent in self.intents:

            for pattern in intent["patterns"]:

                score = self.calculate_score(
                    user_input,
                    pattern
                )

                if score > best_score:
                    best_score = score
                    best_intent = intent

        if best_score >= CONFIDENCE_THRESHOLD:
            return best_intent, best_score

        return None, best_score

    # Handle special commands
    def special_commands(self, user_input):

        text = self.clean_text(user_input)

        # Store user's name
        if text.startswith("my name is "):

            self.user_name = text.replace(
                "my name is ",
                ""
            ).strip().title()

            return (
                f"Nice to meet you, {self.user_name}! 😊",
                "name_storage"
            )

        # Alternative name format
        if text.startswith("call me "):

            self.user_name = text.replace(
                "call me ",
                ""
            ).strip().title()

            return (
                f"Nice to meet you, {self.user_name}! 😊",
                "name_storage"
            )

        # Recall user's name
        if text == "what is my name":

            if self.user_name:

                return (
                    f"Your name is {self.user_name}. 😊",
                    "name_recall"
                )

            return (
                "You haven't told me your name yet.",
                "name_recall"
            )

        # Current time
        if "time" in text:

            current_time = datetime.now().strftime(
                "%I:%M %p"
            )

            return (
                f"The current time is {current_time}. ⏰",
                "time"
            )

        # Current date
        if "date" in text:

            current_date = datetime.now().strftime(
                "%d %B %Y"
            )

            return (
                f"Today's date is {current_date}. 📅",
                "date"
            )

        return None

    # Generate chatbot response
    def get_response(self, user_input):

        # Check for empty input
        if not user_input or not user_input.strip():

            response = "Please enter a message. 😊"

            save_message(
                user_input,
                response,
                "empty"
            )

            return response

        # Check special commands first
        special_response = self.special_commands(
            user_input
        )

        if special_response:

            response, intent = special_response

            save_message(
                user_input,
                response,
                intent
            )

            return response

        # Find matching intent
        intent, score = self.find_intent(
            user_input
        )

        if intent:

            response = random.choice(
                intent["responses"]
            )

            save_message(
                user_input,
                response,
                intent["tag"]
            )

            return response

        # Fallback response
        response = (
            "I'm sorry, I don't understand that yet. 🤔\n"
            "Try asking me about Python, AI, NLP, "
            "programming, studies, projects, or career advice."
        )

        save_message(
            user_input,
            response,
            "unknown"
        )

        return response