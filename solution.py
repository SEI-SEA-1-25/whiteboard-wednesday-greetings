# Make a solution.py that solves the following problem: given a string representing a language 
# (we'll plan for "english", "spanish", and "french"), print out a greeting for that language 
# (in this case: "Hello!" and "Hola!" and "Bonjour!").

greetings = {
    'English': 'Hello',
    'Spanish': 'Hola',
    'French': 'Bonjour'
}
language = input('please enter a language: english, spanish, or french\n').lower()
if language == "english":
  print("Hello!")
elif language == "spanish":
  print("Hola!")
elif language == "french":
  print("Bonjour!")