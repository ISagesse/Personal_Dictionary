import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def definition():
    words = input("Enter a word to define: ")
    if words.lower() in data:
        print(data[words.lower()][0])
        if words.title() in data:
            print(data[words.title()][0])
        elif words.capitalize() in data:
            print(data[words.capitalize()][0])
    elif len(get_close_matches(words, data.keys())) > 0:
        decision = input(f"Did you mean {get_close_matches(words, data.keys())[0]} instead? Please enter yes or no: ")
        if decision == "yes":
            word = get_close_matches(words, data.keys())[0]
            print(data[word][0])
        else:
            print("Please check spelling of the entered input")
    else:
        print("This word is not in our dictionary, please double check the word")

definition()