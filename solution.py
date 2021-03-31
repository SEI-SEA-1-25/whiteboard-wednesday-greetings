# english = "Hello"
# french= "Bonjour"
# spanish = "Hola"

# prompt = '>'
# print('enter your language, user!')
# user_language = input(prompt).lower()


# def greeting(user_language):
#     if(user_language == 'english'):
#         print('Hello!')
#     elif(user_language == 'spanish'):
#         print('Hola!')
#     elif(user_language == 'french'):
#         print('Bonjour!')

# greeting(user_language)


greetings = {
    'english': "Hello!",
    'spanish': "Hola!",
    'french': "Bonjour!",
    'german': "Hallo!",
    'portugese': "Olá",
    'italian': "Ciao",
    'russian': "Privet!",
    'czech': "Ahoj!",
    'finnish': "Hei!",
}

# for greeting in greetings:
#     if ('french' in greeting):
#         print(greetings[greeting])
    # print(greetings[greeting])


prompt = '>'
print('enter your language, user!')
user_language = input(prompt).lower()

def greet(user_language):
    for greeting in greetings:
        if (user_language in greeting):
            print(greetings[greeting])
                
greet(user_language)
