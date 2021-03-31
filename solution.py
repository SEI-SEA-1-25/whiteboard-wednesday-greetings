operation = input("Say hello in English, French, German or Spanish:")

# English
if operation == "hello" or operation == "Hello":
    print(f"Good morning!")
#else if French
elif operation == "bonjour" or operation == "Bonjour":
    print(f"Bonne matinée!")
#else if German
elif operation == "hallo" or operation == "Hallo":
    print(f"Guten Morgen!")
#else if Spanish
elif operation == "hola" or operation == "Hola":
    print(f"Buenos días!")
#catch
else:
    print("Incorrect input 🤔 ")