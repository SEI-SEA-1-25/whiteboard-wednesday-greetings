# given a string representing a language
# (we'll plan for "english", "spanish", and "french"),
# print out a greeting for that language (in this case:
# "Hello!" and "Hola!" and "Bonjour!").

languages = {
  "english": 'Hello',
  "spanish": 'Hola',
  "french": 'Bonjour'
}

user_response = input('Choose a language: English, Spanish, or French\n')
user_response = user_response.lower()

for language in languages:
  if(user_response != language):
    pass
  if(user_response == language):
    print(languages[language])
