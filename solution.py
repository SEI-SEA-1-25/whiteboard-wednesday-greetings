greeting_dictionary = {
    'english': 'Hello!',
    'spanish': 'Hola!',
    'french': 'Bonjour!'
}

user_input = input('please enter a language: english, spanish, or french\n').lower()
for key, value in greeting_dictionary.items():
    if key == user_input:
        print_greeting = value
print(print_greeting) 
