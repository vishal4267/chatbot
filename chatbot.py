import nltk
from nltk.chat.util import Chat, reflections

# Define a list of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by Vishal. You can call me Chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem",]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Nice to hear that", "Alright, great!",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon!",]
    ],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start the conversation
def chatbot_conversation():
    print("Hi, I'm a chatbot. Type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    chatbot_conversation()