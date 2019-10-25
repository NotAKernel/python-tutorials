def show_messages(messages):
    """Shows text messages."""
    for message in messages:
        print(message)

messages = ['Hello, Daniel', 'How are you?']
typed_messages = ['Hello, James', 'I am alright']

def send_messages(typed_messages, delivered_messages):
    """Receives and prints messages."""
while typed_messages:
    sent_messages = typed_messages.pop()
    print("Your message is sending")
    delivered_messages.append(sent_messages)
    for delivered_message in delivered_messages:
         print(delivered_messages)
    
delivered_messages = []

send_messages(typed_messages, delivered_messages)