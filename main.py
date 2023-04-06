# English to Croatian dictionary with 54 words
EtoCroatian = {'I': 'Ja', 'play': 'igrat', 'with': 'sa', 'they': 'oni',
               'soccer': 'nogomet', 'player': 'igrac', 'am': 'sam', 'friends': 'prijatelji', 'and': 'i',
               'ball': 'lopta', 'win': 'pobjedit', 'she': 'ona', 'hockey': 'hokej',
               'basketball': 'kosarka', 'he': 'on', 'lose': 'izgubit', 'hit': 'lupit',
               'shoot': 'pogodit', 'one': 'jedna', 'two': 'dvije', 'three': 'tri', 'four': 'cetri',
               'run': 'trcat', 'walk': 'hodat', 'stop': 'prestat', 'start': 'pocat',
               'is': 'je', 'water': 'voda', 'drink': 'pit', 'jump': 'skocit', 'number': 'broj',
               'tournament': 'turnir', 'team': 'tim', 'coach': 'trener', 'referee': 'sudac',
               'throw': 'bacit', 'goalie': 'golman', 'cleats': 'kopce', 'skates': 'klizaljke',
               'skate': 'klizat', 'stick': 'stap', 'puck': 'pak', 'of': 'od', 'bottle': 'boca',
               'penalty': 'kazna', 'card': 'karta', 'red': 'crvana', 'yellow': 'zuta', 'foul': 'prekrsaj',
               'we': 'mi', 'you': 'ti', 'has': 'imat', 'when': 'kad', 'to': 'za'}


# Function checks which number is in front of the plural word and adds the proper suffix to it for English and Croatian
def count(sentence):
    new = []
    translation = ''
    word = ''
    UCletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCletters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCletters + LCletters

    # Adds words to a list
    for char in sentence:
        if char in letters:
            word += char
        else:
            new.append(word)
            word = ''
    count = 0

    # Finds indexes and checks for which number is before word and adds proper suffix to word
    for each in new:
        if each.lower() == 'dvije' or each.lower() == 'tri' or each.lower() == 'cetri':
            place = count + 1
            word = new[place]
            word = word[:-1] + 'e'
            new.pop(place)
            new.insert(place, word)

        if each.lower() == 'two' or each.lower() == 'three' or each.lower() == 'four':
            place = count + 1
            word = new[place]
            word = word + 's'
            new.pop(place)
            new.insert(place, word)
        count += 1

    # Creates Final sentence and returns it
    for x in new:
        if x != '':
            translation += x
            translation += ' '
    return translation


# Function filters out the English words that are not directly in the dictionaries due to the suffixes or
# capitalization
def filter_out_E(sentence, dictionary):
    new = []
    translation = ''
    word = ''
    UCletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCletters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCletters + LCletters

    # Adds words to a list
    for char in sentence:
        if char in letters:
            word += char
        else:
            new.append(word)
            word = ''

    # Finds indexes then removes suffix and capitalization from word and checks if it is in the dictionary
    for each in new:
        place = new.index(each)
        check = each[:-1]
        check2 = each[:-2]
        check3 = check2 + 's'

        if each not in dictionary.keys():
            if each.lower() in dictionary.keys():
                final = dictionary[each.lower()]
                first = final[0]
                final = first.capitalize() + final[1:]
                new.pop(place)
                new.insert(place, final)

        if check.lower() in dictionary.keys():
            final = dictionary[check.lower()]
            new.pop(place)
            new.insert(place, final)

        if check2.lower() in dictionary.keys():
            final = dictionary[check2.lower()]
            new.pop(place)
            new.insert(place, final)

        if check3.lower() in dictionary.keys():
            final = dictionary[check3.lower()]
            new.pop(place)
            new.insert(place, final)

    # Creates final sentence and returns it
    for x in new:
        if x != '':
            translation += x
            translation += ' '
    return translation


# Function checks for English pronoun being used and adds proper suffix to each word
def pronoun_E(sentence):
    new = []
    translation = ''
    word = ''
    UCletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCletters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCletters + LCletters

    # Adds all words to a list
    for char in sentence:
        if char in letters:
            word += char
        else:
            new.append(word)
            word = ''

    # Finds each index then checks which pronoun is being used and adds the proper suffix to each word
    for each in new:
        place = new.index(each)
        if new[place - 1].lower() == 'he' or new[place - 1].lower() == 'she' and place - 1 >= 0:
            final = each + 's'
            new.pop(place)
            new.insert(place, final)

        if new[place - 1].lower() == 'they' and each[-1] == 's' and place - 1 >= 0:
            final = each[:-1] + 've'
            new.pop(place)
            new.insert(place, final)

    # Creates final sentence and returns it
    for x in new:
        translation += x
        translation += ' '
    return translation


# Function filters out the Croatian words that are not directly in the dictionaries due to the suffixes or
# capitalization
def filter_out_cro(sentence, dictionary):
    new = []
    translation = ''
    word = ''
    UCletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCletters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCletters + LCletters

    # Adds each word to a list
    for char in sentence:
        if char in letters:
            word += char
        else:
            new.append(word)
            word = ''

    # Finds each index and removes each words suffix and capitalization to check if it is in the dictionary
    for each in new:
        place = new.index(each)
        check = each[:-1] + 't'
        check2 = each[:-2] + 't'
        check3 = each[:-1] + 'a'

        if each not in dictionary.keys():
            if each.lower() in dictionary.keys():
                final = dictionary[each.lower()]
                first = final[0]
                final = first.capitalize() + final[1:]
                new.pop(place)
                new.insert(place, final)

        if each + 't' in dictionary.keys():
            final = dictionary[each + 't']
            new.pop(place)
            new.insert(place, final)

        if check in dictionary.keys():
            final = dictionary[check]
            new.pop(place)
            new.insert(place, final)

        if check2 in dictionary.keys():
            final = dictionary[check2]
            new.pop(place)
            new.insert(place, final)

        if check3 in dictionary.keys():
            final = dictionary[check3]
            new.pop(place)
            new.insert(place, final)

    # Creates final sentence and returns it
    for x in new:
        if x != '':
            translation += x
            translation += ' '
    return translation


# function checks for Croatian pronoun being used and attaches appropriate suffix to each word
def pronoun_C(sentence):
    new = []
    translation = ''
    word = ''
    UCletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCletters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCletters + LCletters

    # Loop puts all words in a list
    for char in sentence:
        if char in letters:
            word += char
        else:
            new.append(word)
            word = ''

    # Finds the index of each word then checks the pronoun attached to it and adds the suffix
    for each in new:
        place = new.index(each)
        if new[place - 1].lower() == 'oni' and place - 1 >= 0:
            final = each[:-1] + 'ju'
            new.pop(place)
            new.insert(place, final)

        if new[place - 1] == 'Ja' or new[place - 1] == 'i' and place - 1 >= 0:
            final = each[:-1] + 'm'
            new.pop(place)
            new.insert(place, final)

        if new[place - 1].lower() == 'ona' or new[place - 1] == 'on' and place - 1 >= 0:
            final = each[:-1]
            new.pop(place)
            new.insert(place, final)

        if new[place - 1].lower() == 'ti' and place - 1 >= 0:
            final = each[:-1] + 's'
            new.pop(place)
            new.insert(place, final)

        if new[place - 1].lower() == 'mi' and place - 1 >= 0:
            final = each[:-1] + 'mo'
            new.pop(place)
            new.insert(place, final)

    # Creates the final sentence and returns it
    for x in new:
        translation += x
        translation += ' '
    return translation


# Function creates the reversed dictionary
def reverse_dictionary(dict):
    new = {}
    for word in dict:
        new[dict[word]] = word
    return new
    # Makes the value of new dictionary at the key(equal to the value of each key in old dictionary) equal to the key at
    # the old dictionary(word)
    # The keys in the old dictionary are becoming values and the values are becoming keys for the new dictionary


# Creates the Croatian to English dictionary
CroatiantoE = reverse_dictionary(EtoCroatian)

dicts = {'English to French': EtoCroatian, 'French to English': CroatiantoE}


# Translates a word to the corresponding word in the appropriate dictionary
def translateWord(word, dictionary):
    if word in dictionary.keys():
        return dictionary[word]
    elif word != '':
        return '"' + word + '"'
    return word


def translate(phrase, dicts, direction):
    UCletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCletters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCletters + LCletters
    dictionary = dicts[direction]
    translation = ''
    word = ''

    # Creates sentence then calls function to translate it using appropriate dictionary
    for character in phrase:
        if character in letters:
            word = word + character
        else:
            translation = translation + translateWord(word, dictionary) + character
            word = ''
    translation = translation + translateWord(word, dictionary) + character

    # Fixes glitch with two periods at end of sentence
    translation = translation[:-1]
    if phrase[-1] != '.':
        translation = translation + '.'

    return translation


sentence = 'They have two balls to play soccer with'

# Applies all functions to sentence to fully translate it
translated = translate(sentence, dicts, 'English to French')
translated = filter_out_E(translated, EtoCroatian)
translated = count(translated)
translated = pronoun_C(translated)

print('--------------------------------------')
print('Input:', sentence)
print('Output:', translated)
print('--------------------------------------')

sentence = 'Oni imaju dvije lopte za igrat nogomet sa'

# Applies all functions to sentence to fully translate it
translated = translate(sentence, dicts, 'French to English')
translated = filter_out_cro(translated, CroatiantoE)
translated = count(translated)
translated = pronoun_E(translated)

print('Input:', sentence)
print('Output:', translated)
print('--------------------------------------')
