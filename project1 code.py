import json
import os
import random

class Chatbot:
    def __init__(self, context_file='contextcode.json'):
        self.context_file = context_file
        self.context = self.load_context()
        self.greetings = ["Hello!", "Hi there!", "Greetings!", "Hey!"]
        self.farewells = ["Goodbye!", "See you later!", "Take care!", "Bye!"]
        self.predefined_questions = [
            "What's your name?",
            "How are you feeling today?",
            "What is your favorite color?",
            "Do you like movies?",
            "What's your favorite hobby?"
        ]
        self.responses = {
            "What's your name?": "It's nice to meet you, {}.",
            "How are you feeling today?": "I'm glad to hear you're feeling {}.",
            "What is your favorite color?": "{} is a beautiful color!",
            "Do you like movies?": "I also enjoy watching movies, especially {}.",
            "What's your favorite hobby?": "{} sounds like a lot of fun!"
        }
        self.user_questions = {
            "Hi": "Hi there!",
            "Hello": "Hi there!",
            "Tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
            "Can you tell me a joke?": "Why don't scientists trust atoms? Because they make up everything!",
            "What is your name?": "My name is Karen. I am a virtual assistant.",
            "Where are you located?": "I am a virtual assistant. I am not located anywhere but the Internet",
            "What services do you offer?": "I can chat with you, answer questions, and remember our past conversations.",
            "How are you?": "I am feeling great.",
            "hi": "Hi there!",
            "hello": "Hi there!",
            "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
            "can you tell me a joke?": "Why don't scientists trust atoms? Because they make up everything!",
            "what is your name?": "My name is Karen. I am a virtual assistant.",
            "where are you located?": "I am a virtual assistant. I am not located anywhere but the Internet",
            "what services do you offer?": "I can chat with you, answer questions, and remember our past conversations.",
            "how are you?": "I am feeling great.",

        }

    def load_context(self):
        if os.path.exists(self.context_file):
            with open(self.context_file, 'r') as file:
                return json.load(file)
        return []

    def save_context(self):
        with open(self.context_file, 'w') as file:
            json.dump(self.context, file)

    def greet(self):
        greeting = random.choice(self.greetings)
        self.context.append(greeting)
        print(greeting)
        self.save_context()

    def ask_predefined_questions(self):
        for question in self.predefined_questions[:3]:
            self.context.append(question)
            print(question)
            user_input = input("You: ")
            self.context.append(user_input)
            self.respond_to_predefined_question(question, user_input)
            self.save_context()

    def respond_to_predefined_question(self, question, user_input):
        if question in self.responses:
            response = self.responses[question].format(user_input)
            self.context.append(response)
            print(response)
            self.save_context()
        else:
            self.handle_unknown_input()

    def handle_unknown_input(self):
        friendly_response = "I'm sorry, I didn't quite understand that. Could you please rephrase?"
        self.context.append(friendly_response)
        print(friendly_response)
        self.save_context()

    def farewell(self):
        farewell = random.choice(self.farewells)
        self.context.append(farewell)
        print(farewell)
        self.save_context()

    def recall_context(self):
        print("\nHere's a summary of our previous conversation(s):")
        for message in self.context:
            print(message)

    def handle_user_question(self, user_question):
        if user_question in self.user_questions:
            response = self.user_questions[user_question]
            self.context.append(response)
            print(response)
        else:
            self.handle_unknown_input()
        self.save_context()

# Run the chatbot
chatbot = Chatbot()
chatbot.greet()
chatbot.ask_predefined_questions()
while True:
    user_question = input("You: ")
    if user_question.lower() in ["exit", "quit", "goodbye", "bye"]:
        chatbot.farewell()
        break
    else:
        chatbot.handle_user_question(user_question)
chatbot.recall_context()
