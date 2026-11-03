# Mike Goodman 
# Sending Messages 
# 4/10 

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()

        print(current_message)

        sent_messages.append(current_message)

text_messages = [
    "Hello!",
    "How are you?",
    "See you later!"
]

sent_messages = []

send_messages(text_messages, sent_messages)

print("\nOriginal messages:")
print(text_messages)

print("\nSent messages:")
print(sent_messages)