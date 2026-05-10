import time

def greet_user():
    print("Hello! Welcome to our store. How can I assist you today?")
    time.sleep(1)

def handle_query(query):
    query = query.lower()

    if "store hours" in query or "open hours" in query:
        return "Our store is open from 9 AM to 9 PM, Monday to Saturday."
    elif "products" in query or "catalog" in query:
        return "We offer a wide range of products including electronics, clothing, and home goods. What would you like to know about?"
    elif "location" in query or "address" in query:
        return "We are located at 123 Main Street, YourCity, YourState."
    elif "contact" in query or "support" in query:
        return "You can contact us at support@ourstore.com or call us at (123) 456-7890."
    elif "thank you" in query or "bye" in query:
        return "You're welcome! Feel free to reach out if you have any more questions. Goodbye!"
    else:
        return "Sorry, I didn't quite understand that. Can you please rephrase?"

def start_chat():
    greet_user()
    
    while True:
        user_input = input("\nYou: ")
        
        if "bye" in user_input.lower() or "exit" in user_input.lower():
            print("Bot: Goodbye! Have a great day!")
            break
        
        response = handle_query(user_input)
        print("Bot:", response)

# Start the chatbot interaction
start_chat()
