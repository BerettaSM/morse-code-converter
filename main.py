import logging
import os
import sys
from time import sleep

import pyinputplus as pyip
from playsound import playsound

logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(message)s')

# ---------- CONSTANTS ----------
CURRENT_DIR = os.path.abspath('.')
DAH_SOUND = os.path.join(CURRENT_DIR, 'sounds/dah.wav')
DIT_SOUND = os.path.join(CURRENT_DIR, 'sounds/dit.wav')
SPACE = ' '
LETTER_SEP = 3 * SPACE
WORD_SEP = 7 * SPACE
MORSE_DICT = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
              'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
              'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
              'y': '-.--', 'z': '--..', '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', '/': '-..-.',
              '(': '-.--.', ')': '-.--.-', '\'': '.----.', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
              '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', '1': '.----',
              '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
              '9': '----.', '0': '-----'}
# -------------------------------


def to_morse_str(string: str) -> str:
    return WORD_SEP.join(
        [
            LETTER_SEP.join(
                [MORSE_DICT[symbol] for symbol in word if symbol in MORSE_DICT]
            )
            for word in string.lower().split()
        ]
    )


def play_morse_str(morse_str: str) -> None:
    logging.info("Started playing.")
    for char in morse_str:
        if char == '.':
            playsound(sound=DIT_SOUND)
        elif char == '-':
            playsound(sound=DAH_SOUND)
        else:
            sleep(0.1)
    logging.info("Finished playing.")


def print_waiting_dots(num: int) -> None:
    for n in range(num):
        print('.', end='')
        sleep(0.5)
    print()


def print_header():
    title = " MORSE CODE CONVERTER "
    exit_info = " Press CTRL + C to Exit at any time. "
    fill = "="
    length = len(title) * 2
    print(fill*length*2)
    print(title.center(length*2, fill))
    print(fill * length * 2)
    print(exit_info.center(length * 2, fill))
    print(fill * length * 2)


def clear_console():
    if sys.platform == 'win32':
        os.system('cls')
    elif sys.platform in ['linux', 'linux2', 'darwin']:
        os.system('clear')


def main():
    while True:
        clear_console()
        print_header()
        string = pyip.inputStr(prompt="Enter a string to be converted into morse code: ")
        morse_str = to_morse_str(string)
        print("Computing", end='')
        print_waiting_dots(3)
        print(f"Your input translated to morse code is: \n\n{morse_str}\n\n")
        play = pyip.inputStr(prompt='Play the sound? [yes/no]: ')
        if play == 'yes':
            play_morse_str(morse_str=morse_str)
        should_convert_another = pyip.inputStr(prompt='Make more conversions? [yes/no]: ')
        if should_convert_another == 'no':
            break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n-= Program Interrupted by the User =-")
    else:
        print("\n\n-= End of Program =-")
