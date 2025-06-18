import random

class RuleBot:
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    # Define casual and fun random questions and responses
    random_questions_responses = {
        "hi": "Hey there! How's your day going?",
        "hello": "Hi! Ready for a fun chat?",
        "how are you?": "I'm doing great, thanks for asking! What about you?",
        "what's your name?": "I'm RuleBot, your friendly chatbot!",
        "what can you do?": "I can chat with you, tell you fun facts, jokes, and answer general questions!",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "what is the time?": "I'm not wearing a watch  Try checking your device clock!",
        "what's the weather like?": "I can't check live weather, but I hope it's sunny where you are!",
        "what is ai?": "AI stands for Artificial Intelligence — like me! I try to understand and respond to you.",
        "what is your favorite color?": "I like blue — it reminds me of the sky and calmness.",
        "tell me something interesting": "Octopuses have three hearts and blue blood!",
        "do you sleep?": "Nope, I'm always awake and ready to chat!",
        "what is your hobby?": "I like chatting with awesome people like you!",
        "who created you?": "I was created by clever developers who love AI and coding!",
        "can you sing?": "I'd love to, but I might sound robotic  Beep bop!",
        "what's your favorite food?": "Electricity and data bytes — yum! ",
        "can you dance?": "Only in binary  01010101!",
        "do you have emotions?": "Not really, but I try to understand how you're feeling!",
        "why is the sky blue?": "Because of the way sunlight scatters in the atmosphere. Science is cool!",
        "do you believe in aliens?": "Who knows? The universe is huge! ",
        "tell me a fun fact": "Bananas are berries, but strawberries aren't!",
        "thank you": "You're welcome! Let's chat again soon.",
        "no thanks": "Alright! I'm here if you need me.",
        "bye": "Goodbye! It was fun chatting with you "
    }

    def __init__(self):
        self.greeted = False

    def greet(self):
        if not self.greeted:
            print("Hello! I'm RuleBot, your fun chat companion. Ask me anything or just say hi!")
            self.greeted = True

    def get_response(self, user_input):
        user_input_lower = user_input.lower()

        if user_input_lower in self.exit_commands:
            print("Goodbye! Have a great day!")
            return True  # Ends the chat

        for question, response in self.random_questions_responses.items():
            if question in user_input_lower:
                print(response)
                return False

        if user_input_lower in self.negative_responses:
            print("Sorry to hear that. Want to talk about something fun?")
        else:
            print("Hmm, I’m not sure how to respond to that. Try asking me something else!")

        return False

    def start_chat(self):
        self.greet()
        while True:
            user_input = input("You: ")
            if self.get_response(user_input):
                break

# Start the chatbot
if __name__ == "__main__":
    rule_bot = RuleBot()
    rule_bot.start_chat()
