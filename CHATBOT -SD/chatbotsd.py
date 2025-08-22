class Preprocessor:
    def clean_input(self, text):
        return text.strip().lower()


class Responder:
    def __init__(self):
        self.departments = {
            "1": "Billing",
            "2": "Technical Support",
            "3": "Sales",
            "4": "General Inquiry"
        }

    def generate_response(self, cleaned_text):
        if cleaned_text == "hi":
            return "Hi, welcome to customer service."
        elif cleaned_text == "how are you":
            return "Good, what about you?"
        elif cleaned_text == "i have a problem":
            return self.get_department_options()
        elif cleaned_text in self.departments:
            return f"Directing you to {self.departments[cleaned_text]}. Thank you. Anything else?"
        elif cleaned_text in ["no", "bye"]:
            return "End chat"
        elif cleaned_text == "yes":
            return self.get_department_options()
        else:
            return "Sorry, I didn't understand that."

    def get_department_options(self):
        return ("Please select the department:\n"
                "1. Billing\n"
                "2. Technical Support\n"
                "3. Sales\n"
                "4. General Inquiry")


class ChatBot:
    def __init__(self):
        self.preprocessor = Preprocessor()
        self.responder = Responder()

    def chat(self):
        print("ChatBot: Hello! Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            cleaned = self.preprocessor.clean_input(user_input)
            response = self.responder.generate_response(cleaned)
            print("ChatBot:", response)
            if response == "End chat":
                break


# Run the chatbot
if __name__ == "__main__":
    bot = ChatBot()
    bot.chat()
