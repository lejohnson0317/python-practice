def send_messages(messages):
    """Sends given message to user"""
    while messages:
        current_message = messages.pop()
        print (current_message)
        sent_messages.append(current_message)


messages = ['Have a great day!', 'Nice to meet you!', 'It was really nice to meet you.']
sent_messages =  []

send_messages(messages)
print ("Messages that have been sent so far are:\n", sent_messages)
print ("Messages in the original list are: \n", messages)