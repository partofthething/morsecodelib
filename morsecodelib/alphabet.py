# -*- coding: utf-8 -*-
"""
Lookup table for all of Morse code.
"""

letters_to_code = {'A': '.-',
                   'B': '-...',
                   'C': '-.-.',
                   'D': '-..',
                   'E': '.',
                   'F': '..-.',
                   'G': '--.',
                   'H': '....',
                   'I': '..',
                   'J': '.---',
                   'K': '-.-',
                   'L': '.-..',
                   'M': '--',
                   'N': '-.',
                   'O': '---',
                   'P': '.--.',
                   'Q': '--.-',
                   'R': '.-.',
                   'S': '...',
                   'T': '-',
                   'U': '..-',
                   'V': '...-',
                   'W': '.--',
                   'X': '-..-',
                   'Y': '-.--',
                   'Z': '--..',
                   '0': '-----',
                   '1': '.----',
                   '2': '..---',
                   '3': '...--',
                   '4': '....-',
                   '5': '.....',
                   '6': '-....',
                   '7': '--...',
                   '8': '---..',
                   '9': '----.',
                   ' ': ' ',
                   ',': '--..--',
                   '.': '.-.-.-',
                   '?': '..--..',
                   ';': '-.-.-.',
                   ':': '---...',
                   "'": '.----.',
                   '-': '-....-',
                   '/': '-..-.',
                   '(': '-.--.-',
                   ')': '-.--.-',
                   '_': '..--.-',
                   '!': '-.-.--',
                   'À': '.--.-',
                   'Å': '.--.-',
                   'Ä': '.-.-,',
                   'Æ': '.-.-',
                   'É': '..-..',
                   'È': '.-..-',
                   'Ö': '---.',
                   'Ø': '---.',
                   'Þ':'.--..',
                   'Ü': '..--',
                   }

# build reverse lookup too
code_to_letters = {}
for letter, code in letters_to_code.items():
    code_to_letters[code] = letter
