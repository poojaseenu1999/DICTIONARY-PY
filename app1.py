import json

data = json.load(open("data.json",))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "this word doesnt exist!"


word = input("enter the word: ")

print(translate(word))
