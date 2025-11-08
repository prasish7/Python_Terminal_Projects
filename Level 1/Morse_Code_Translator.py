
# MORSE_CODE_DICT = {
#     'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
#     'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
#     'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
#     'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
#     'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
#     'Z': '--..', 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
#     'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
#     'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
#     'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 
#     'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
#     'z': '--..',
#     '0': '-----', '1': '.----', '2': '..---', '3': '...--',
#     '4': '....-', '5': '.....', '6': '-....', '7': '--...',
#     '8': '---..', '9': '----.',
#     '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-',
#     '(': '-.--.', ':': '---...', ',': '--..--', '=': '-...-',
#     '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '+': '.-.-.',
#     '"': '.-..-.', '?': '..--..', '/': '-..-.', ' ': '/'
# }

# # print(MORSE_CODE_DICT.items())

# REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}
# # REVERSE_MORSE_CODE_DICT = {}
# # for k, v in MORSE_CODE_DICT.items():
# #     REVERSE_MORSE_CODE_DICT[v] = k
# # print(REVERSE_MORSE_CODE_DICT.items())


# text = input("Enter text or Morse code: ").strip()

# if all(c in " .-/ " for c in text):
#     decoded = ''
#     for code in text.split(' '):
#         decoded += REVERSE_MORSE_CODE_DICT.get(code, '')
#     print("Decoded text:", decoded)
# else:
#     encoded = ''    
#     for char in text:
#         encoded += MORSE_CODE_DICT.get(char, '') + ' '
#     print("Encoded Morse:", encoded.strip())
