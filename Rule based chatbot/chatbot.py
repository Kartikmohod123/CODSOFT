import random
import re

class RuleBot:
    # Predefined responses
    negative_res = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    random_question = (
        "Why are you here?",
        "Are there many humans like you?",
        "What do you consume for sustenance?",
        "Is there intelligent life on this planet?",
        "Does Earth have a leader?"
    )

    def __init__(self):
        # Decision tree - keyword recognition (regex)
        self.alienbabble = {
            'describe_planet_intent': r'.*\s*your planet.*',
            'answer_why_intent': r'why\sare.*',
            'about_intellipaat': r'.*\s*intellipaat.*',
            'faq_hours': r'.*\b(hours|timing)\b.*',
            'faq_location': r'.*\b(location|where)\b.*',
        }
        # Fixed Q&A
        self.faq_responses = {
            'faq_hours': "We are available 24/7 for learners around the globe!",
            'faq_location': "We are based online and accessible from anywhere on Earth."
        }
        # Supported languages (manual rule mapping)
        self.multi_language_support = {
            'hola': "¡Hola! ¿Cómo puedo ayudarte?",
            'bonjour': "Bonjour! Comment puis-je vous aider?"
        }

    def greet(self):
        # Form filling
        self.name = input("👽 What is your name?\n")
        self.email = input("📧 What is your email?\n")
        will_help = input(f"\nHi {self.name}, I am Bot. Will you help me learn about your planet?\n")

        if will_help.lower() in self.negative_res:
            print("👋 Have a nice Earth day!")
            return

        # Menu-based interaction
        self.show_menu()

    def show_menu(self):
        print("\n🔘 Choose an option to begin:")
        print("1. Chat about Earth")
        print("2. Ask a question")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            self.chat()
        elif choice == "2":
            self.ask_question()
        elif choice == "3":
            print("👋 Goodbye!")
        else:
            print("❌ Invalid option. Try again.")
            self.show_menu()

    def make_exit(self, reply):
        if reply.lower() in self.exit_commands:
            print("👋 Have a nice day!")
            return True
        return False

    def chat(self):
        reply = input("💬 " + random.choice(self.random_question) + "\n").lower()
        while not self.make_exit(reply):
            # Check for language-based responses
            for word in self.multi_language_support:
                if word in reply:
                    print("🌐", self.multi_language_support[word])
                    break
            reply = input("💬 " + self.match_reply(reply))

    def ask_question(self):
        question = input("🤖 Ask your question:\n").lower()
        print("💬 " + self.match_reply(question))
        self.show_menu()  # Return to menu

    def match_reply(self, reply):
        # Keyword recognition + Decision tree logic
        for intent, regex_pattern in self.alienbabble.items():
            found_match = re.match(regex_pattern, reply)
            if found_match:
                if intent in self.faq_responses:
                    return self.faq_responses[intent]
                elif intent == 'describe_planet_intent':
                    return self.describe_planet_intent()
                elif intent == 'answer_why_intent':
                    return self.answer_why_intent()
                elif intent == 'about_intellipaat':
                    return self.about_intellipaat()
        return self.no_match_intent()

    def describe_planet_intent(self):
        responses = (
            "🌍 My planet is a utopia of diverse organisms.",
            "🌎 I heard the coffee is good here!"
        )
        return random.choice(responses)

    def answer_why_intent(self):
        responses = (
            "🛸 I come in peace.",
            "📡 I am here to collect data on your planet and its inhabitants.",
            "☕ I heard the coffee is good!"
        )
        return random.choice(responses)

    def about_intellipaat(self):
        responses = (
            "📘 Intellipaat is the world's largest professional educational company.",
            "💡 Intellipaat helps you learn concepts like never before.",
            "🚀 Intellipaat is where your career and skills grow."
        )
        return random.choice(responses)

    def no_match_intent(self):
        # Fallback response
        responses = (
            "🤔 Please tell me more.",
            "🧐 Interesting. Can you elaborate?",
            "😲 I see. How do you think?",
            "❓ Why?",
            "🤷 How do you think I feel when you say that?"
        )
        return random.choice(responses)

# Run the chatbot
if __name__ == "__main__":
    bot = RuleBot()
    bot.greet()
