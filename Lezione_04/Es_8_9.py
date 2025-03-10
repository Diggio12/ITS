messages:list = ['Come va?', 'Hai terminato?', 'Ciao!', 'Chi sei?']

def show_messages(list:list):
    for i in list:
        print(i)

if __name__ == '__main__':
    show_messages(messages)