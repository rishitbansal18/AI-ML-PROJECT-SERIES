import json
import os
import random

class AdmissionChatbot:
    def __init__(self, context_file='admission..context.json'):
        self.context_file = context_file
        self.context = self.load_context()
        self.greetings = [
            "Hello! How can I assist you with your college admission queries today?", 
            "Hi there! Need help with college admissions?", 
            "Greetings! How can I help you with your admission process?"
        ]
        self.farewells = [
            "Goodbye! Best of luck with your admissions!", 
            "See you later! Feel free to ask any more questions.", 
            "Take care! Don't hesitate to ask if you have more questions.", 
            "Bye! Wishing you all the best with your college application."
        ]
        self.admission_info = {
            "procedure": "The admission procedure involves submitting an online application, and providing necessary documents. Check the college website for detailed steps.",
            "requirements": "The admission requirements include high school transcripts, letters of recommendation, a personal statement, and standardized test scores of JEE MAINS Examination",
            "deadlines": "The application deadlines vary by program. Generally, the deadlines are around August 15th for early admission and September 15th for regular admission.",
            "campus size": "The college campus size is around 170 acres and is filled with lush green parks and modern infrasturcture.",
            "placements": "The college has a very great record of placements with average package of 15 lakhs per annum.",
            "available courses": "Our college offers MBA, BTech Programs and MTech Programs.",
            "location": "Our College is located in New Delhi,Rohini.",
            "course duration": "The course duration of MBA is 2 Years, BTech is of 4 Years and MTech is of 2 Years."
        }
        self.user_data = {}
        self.error_message = "I'm sorry, I didn't quite understand that. Could you please rephrase or ask about admission procedures, requirements, deadlines, placements or campus?"

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
        self.context.append({"role": "chatbot", "message": greeting})
        print(greeting)
        self.save_context()

    def farewell(self):
        farewell = random.choice(self.farewells)
        self.context.append({"role": "chatbot", "message": farewell})
        print(farewell)
        self.save_context()

    def handle_user_question(self, user_question):
        if "procedure" in user_question.lower():
            response = self.admission_info["procedure"]
        elif "requirement" in user_question.lower():
            response = self.admission_info["requirements"]
        elif "deadline" in user_question.lower():
            response = self.admission_info["deadlines"]
        elif "placements" in user_question.lower():
            response = self.admission_info["placements"]
        elif "campus size" in user_question.lower():
            response = self.admission_info["campus size"]
        elif "available courses" in user_question.lower():
            response = self.admission_info["available courses"]
        elif "course duration" in user_question.lower():
            response = self.admission_info["course duration"]
        else:
            response = self.error_message

        self.context.append({"role": "user", "message": user_question})
        self.context.append({"role": "chatbot", "message": response})
        print(response)
        self.save_context()

    def ask_user_details(self):
        if "name" not in self.user_data:
            print("May I know your name?")
            self.user_data["name"] = input("You: ")
            self.context.append({"role": "user", "message": self.user_data["name"]})
            self.context.append({"role": "chatbot", "message": f"Nice to meet you, {self.user_data['name']}!"})
            print(f"Nice to meet you, {self.user_data['name']}!")
            self.save_context()
        
        if "interested_program" not in self.user_data:
            print("Which program are you interested in?")
            self.user_data["interested_program"] = input("You: ")
            self.context.append({"role": "user", "message": self.user_data["interested_program"]})
            self.context.append({"role": "chatbot", "message": f"Great! {self.user_data['interested_program']} is a fantastic choice!"})
            print(f"Great! {self.user_data['interested_program']} is a fantastic choice!")
            self.save_context()

    def recall_context(self):
        print("\nHere's a summary of our previous conversation(s):")
        for message in self.context:
            role = message['role']
            msg = message['message']
            print(f"{role.capitalize()}: {msg}")



chatbot = AdmissionChatbot()
chatbot.greet()
chatbot.ask_user_details()
while True:
    user_question = input("You: ")
    if user_question.lower() in ["exit", "quit", "goodbye", "bye"]:
        chatbot.farewell()
        break
    else:
        chatbot.handle_user_question(user_question)
chatbot.recall_context()
