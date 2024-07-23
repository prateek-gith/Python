import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define some conversation starters and responses
conversation_starters = ["hello", "hi", "hey", "howdy", "yo"]
responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! What can I do for you?",
    "hey": "Hey! How can I assist you today?",
    "howdy": "Howdy! What can I do for you?",
    "yo": "Yo! How can I assist you today?"
}

# Function to generate a response
def generate_response(input_text):
    input_text = input_text.lower()  # Convert input to lowercase
    doc = nlp(input_text)  # Process the input text with spaCy
    # Check if input is a conversation starter
    if input_text in conversation_starters:
        return responses.get(input_text)
    # If not a conversation starter, respond with a generic message
    return "Hmm... I'm not sure how to respond to that. Can you please provide more details?"

# Main function to run the chatbot
def chatbot():
    print("Chatbot: Hello! I'm your chatbot assistant. How can I help you today?")
    while True:
        user_input = input("You: ")  # Get user input
        if user_input.lower() == "exit":  # Allow user to exit the chat
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = generate_response(user_input)  # Generate response
        print("Chatbot:", response)  # Print response

if __name__ == "__main__":
    chatbot()  # Run the chatbot
