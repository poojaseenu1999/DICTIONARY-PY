import json
from difflib import get_close_matches

data = json.load(open("data.json",))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn =input("Did you mean %s instead?enter y if yes or n if no:"   % get_close_matches(w, data.keys())[0])
        if yn == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'n':
            return "The word doesnt exist. please check it."
        else:
             return "sorry! we can't understand your entry."

    else:
        return "This word doesnt exist!please try again!"


word = input("enter the word: ")

output = translate(word)
if type(output) == list:
    for item in output:
       print(item)
else:
      print(output)
