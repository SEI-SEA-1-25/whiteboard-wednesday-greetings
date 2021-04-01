
# language = input("What language does the person speak?").lower()
# # using a dictionary
# dictionary = {
#   "english": "Hello!",
#   "spanish": "Hola!",
#   "french": "Bonjour!",
#   "german": "Hallo!"
# }

# print(dictionary[language])

operation = input("Say hello in English, French, German or Spanish:")
# you can add .low to line above to deal with upper and lower case inputs

# English
if operation == "hello" or operation == "Hello":
    print(f"Good morning! 🇺🇸 🇬🇧 🏴󠁧󠁢󠁳󠁣󠁴󠁿")
#else if French
elif operation == "bonjour" or operation == "Bonjour":
    print(f"Bonne matinée! 🇫🇷 🇨🇩 🇨🇦")
#else if German
elif operation == "hallo" or operation == "Hallo":
    print(f"Guten Morgen! 🇩🇪 🇦🇹 🇨🇭")
#else if Spanish
elif operation == "hola" or operation == "Hola":
    print(f"Buenos días! 🇪🇸 🇲🇽 🇦🇷")
#catch
else:
    print("Incorrect input 🤔 ")



####################### GIVEN SOLUTION #######################
# language = input("What language does the person speak?").lower()

# # using a dictionary
# dictionary = {
#   "english": "Hello!",
#   "spanish": "Hola!",
#   "french": "Bonjour!",
# }

# print(dictionary[language])

# # using if/elif
# if language == "english":
#   print("Hello!")
# elif language == "spanish":
#   print("Hola!")
# elif language == "french":
#   print("Bonjour!")

