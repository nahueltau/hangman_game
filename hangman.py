import sys
sys.path.append('./')
from hangman_imports.functions import get_a_word, format_word, greet_player, firs_and_last_letters, tilde, play_again, get_significado
from hangman_imports import request

racha = 0
rematch = True

def main():
    global rematch
    global racha
    live_count = 5
    possible_letters = "abcdefghijklmnñopqrstuvwxyzáéíóú"

    # setup
    word_to_guess = get_a_word(possible_letters)

    letters_shown = firs_and_last_letters(word_to_guess)

    word_with_holes = format_word(letters_shown, word_to_guess)

    # start
    greet_player(word_with_holes)

    while 0 < word_with_holes.count("_") and live_count > 0:

        letra = input("\nElige una letra: ").lower()

        # cheat
        if(letra == "hint"):
            print(word_to_guess)
        # cheat

        if len(letra) > 1:
            print("Elige una sola letra: ")

        elif letra not in possible_letters:
            print("Elige una letra válida: ")

        elif letra in letters_shown:
            print("Esa letra ya esta descubierta!")

        elif letra in word_to_guess or tilde(letra) in word_to_guess:

            letters_shown.append(letra)
            if letra in "áéíóúaeiou":
                letters_shown.append(tilde(letra))

            word_with_holes = format_word(letters_shown, word_to_guess)

            print("CORRECTO!\n")
            if word_with_holes.count("_") > 0:
                print(word_with_holes+"\n")

        else:
            live_count -= 1
            print("\nLetra incorrecta :(")
            if live_count > 0:
                print("Te quedan "+str(live_count)+" intentos")

    if(live_count == 0):
        print(f"\nPerdiste, la palabra era: {word_to_guess.upper()}\nVer significado -> https://dle.rae.es/{word_to_guess}")
        racha = 0
    else:
        print(f"##########\n Ganaste! \n##########\n\n La palabra era: {word_to_guess.upper()}\nVer significado -> https://dle.rae.es/{word_to_guess}")
        racha += 1
        if racha == 1:
            print(f"GANASTE {str(racha)} JUEGO!\n")
        else:
            print(f"GANASTE {str(racha)} JUEGOS CONSECUTIVOS!!\n")
    
    ver_significado = get_significado()
    if ver_significado:
        significado = request.search_word(word_to_guess)
        print(significado)

    rematch = play_again()
    

while rematch:
    main()
