messages:list = ['Come va?', 'Hai terminato?', 'Ciao!', 'Chi sei?']
sent_messages:list = []

def show_messages():
    for i in messages:
        print(i)
        sent_messages.append(i)
    messages.clear()

show_messages()
print(messages)
print(sent_messages)