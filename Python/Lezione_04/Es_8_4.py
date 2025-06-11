def make_shirt(size, text):
    print(f'The size selected is: {size}. The text displayed will be: {text}')

size_L:str = 'L'
text_default:str = 'I love Python'

make_shirt(size_L, text_default)

size_M:str = 'M'

make_shirt(size_M, text_default)

size:str = input('Insert your size: ')
text:str = input('Insert the text you want printed: ')

make_shirt(size, text)