import random


def remove_line_break(word):
    return word[0:len(word)-1]


def format_word(letters_shown, word_to_guess):
    word_with_holes = ""
    for letter in word_to_guess:
        if letter in letters_shown:
            word_with_holes += letter
        else:
            word_with_holes += "_"
    return remove_line_break(word_with_holes)


def tilde(char):
    vowels = {"a": "á", "e": "é", "i": "í", "o": "ó", "u": "ú",
              "á": "a",  "é": "e",  "í": "i", "ó": "o", "ú": "u", }
    char_til = char
    if char in vowels.keys():
        char_til = vowels.get(char)
    return char_til


def firs_and_last_letters(word):
    first_and_last = [word[0], word[len(word)-2]]
    first_and_last.extend([tilde(word[0]), tilde(word[len(word)-2])])
    return first_and_last


def retrieve_dict_page(letter):
    file = open(f"diccionario/palabras_{letter}.txt", "r", encoding='utf8')
    page = file.readlines()
    file.close()
    return page


def get_random_word(source, min_word_length):
    word = source[random.randint(0, len(source)-1)]
    while len(word) < min_word_length or 0 <= word.find(" ") or 0 <= word.find("-"):
        word = source[random.randint(0, len(source)-1)]
    return word


def get_a_word(possible_letters):
    start_letter = possible_letters[random.randint(0, 26)]
    dict_page = retrieve_dict_page(start_letter)
    word = get_random_word(dict_page, 6)
    return word


def greet_player(word_with_holes):
    print("\nJUEGO: EL AHORACADO")
    print("Adivina la sigueinte palabra, puedes equivocarte 5 veces.")
    print("Presiona Ctrl+C para salir\n")
    print("La palabra a adivinar es: ")
    print(word_with_holes)

def yes_check(input, callback):
    if input.lower() == "si" or input.lower() == "sí" or input.lower() == "s" or input.lower() == "yes" or input.lower() == "y":
        return True
    elif input.lower() == "no" or input.lower() == "n" or input.lower() == "no":
        return False
    else:
        return callback()

def get_significado():
    r = input("Ver significado? (s/n)")
    r = r.strip()
    return yes_check(r, get_significado)

def play_again():
    replay = input("\nJugar de nuevo? (s/n)")
    replay = replay.strip()
    return yes_check(replay, play_again)


def string_encode(string):
    return string.encode("utf-8")


""" 
while True:
    x = input("Give me a letter: ")
    print(string_encode(x))
 """

"""     Give me a letter: á é í ó ú
b'\xc3\xa1 \xc3\xa9 \xc3\xad \xc3\xb3 \xc3\xba \x61'.decode()
b'0xc30xba'.decode() 
"""
