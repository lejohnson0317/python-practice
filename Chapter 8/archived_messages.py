def show_messages(messages):
    """Shows given messge to user"""
    print("Showing all messages:\n")
    for message in messages:
        print (message)

def send_messages(send_message, sent_message):
    """Sends the messages"""
    print("\nSending all messages. Please wait...")
    while send_message:
        current_message = send_message.pop()
        print(f"Sending: {current_message}")
        sent_message.append(current_message)


send_message = ['Have a great day!', 'Nice to meet you!', 'It was really nice to meet you.']
sent_message = []

show_messages(send_message)
send_messages(send_message[:], sent_message)

print("The messages that have been sent are as follows:\n", sent_message)
print("\n\nThe messages from the original list are:\n", send_message)