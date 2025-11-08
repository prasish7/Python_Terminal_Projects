print("Please enter your name: ")
user_name = input().strip()
print(f"Hello, {user_name}! How can I assist you today?")
print("I can assist you with the following:")
print("- Tell me a joke")
print("- What's the weather like?")
print("- Give me a fun fact")
print("- Exit or Quit to end the chat")
user_input = input().strip().lower()
isRunning = True

while isRunning:
    if  user_input == "hello" or user_input == "hi":
        print("Hello! How can I help you today?")

    elif user_input == "what's the weather like?" or user_input == "whats the weather like?" or user_input == "weather" or user_input == "tell me the weather" or user_input == "give me the weather" or user_input == "weather update" or user_input == "current weather" or user_input == "weather report":
        print("I'm sorry, I can't provide real-time weather updates right now.")
    elif user_input == "give me a fun fact" or user_input == "fun fact"or user_input == "tell me a fun fact" or user_input == "i want a fun fact" or user_input == "share a fun fact" or user_input == "fact":
        print("Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!")
    elif user_input == "help":
        print("I can assist you with the following:")
        print("- Tell me a joke")
        print("- What's the weather like?")
        print("- Give me a fun fact")
        print("- Exit or Quit to end the chat")
    elif user_input == "tell me a joke" or user_input == "joke" or user_input == "i want to hear a joke" or user_input == "make me laugh" or user_input == "share a joke":
        print("Why don't scientists trust atoms? Because they make up everything!")
    else:
        print("I'm sorry, I didn't understand that. Please try again or type 'help' for options.")    
    print("What else can I help you with?")
    user_input = input().strip().lower()
    if user_input == "exit" or user_input == "quit":
        print("Goodbye! Have a great day!")
        isRunning = False
        break

