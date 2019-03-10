import json
from difflib import get_close_matches

data = json.load(open('JSON\dictionary.json'))


def definition(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:  # if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data:  # in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        print('Did you mean:')
        matches = get_close_matches(w, data.keys())
        for i in matches:
            print(f'{i}, ', end="")
        return ''
    else:
        return "The word doesn't exist, please double check it."


command = ''
while command != 'q' or 'Q':
    command = command.lower()
    print('''To enter a word type E
To quit type Q''')
    command = input('>>>')
    if command == 'e':
        word = input('Enter a word: ')
        output = definition(word)
        if type(output) == list:
            n = 1
            for i in output:
                print(f'{n}. {i}')
                n += 1
            print('')
        else:
            print(output)
    elif command == 'q':
        print('Good Bye')
        break
    else:
        print('You have typed wrong command, try again.')
