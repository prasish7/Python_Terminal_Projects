
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-',
    '(': '-.--.', ':': '---...', ',': '--..--', '=': '-...-',
    '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '+': '.-.-.',
    '"': '.-..-.', '?': '..--..', '/': '-..-.', ' ': '/'
}
Reverse_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def encode_to_morse(text, shift):
    shifted_dict = {}
    morse_values = list(MORSE_CODE_DICT.values())
    for i, (char, morse) in enumerate(MORSE_CODE_DICT.items()):
        new_index = (i + shift) % len(morse_values)
        shifted_dict[char] = morse_values[new_index]
    
    encoded_message = ' '.join(shifted_dict.get(char, char) for char in text)
    return encoded_message
def decode_from_morse(morse_code, shift):
    shifted_dict = {}
    morse_values = list(MORSE_CODE_DICT.values())
    for i, (char, morse) in enumerate(MORSE_CODE_DICT.items()):
        new_index = (i - shift) % len(morse_values)
        shifted_dict[morse_values[new_index]] = char
    
    decoded_message = ''.join(shifted_dict.get(code, code) for code in morse_code.split(' '))
    return decoded_message
choice = input("Would you like to encode or decode a message? (e/d): ").strip().upper()
if choice not in ['E', 'D']:
    print("Invalid choice. Please enter 'e' to encode or 'd' to decode.")
    exit()
message = input("Enter your message: ")
shift = int(input("Enter the shift number (1-25): "))
if shift < 1 or shift > 25:
    print("Invalid shift number. Please enter a number between 1 and 25.")
    exit()
if choice == 'E':
    final_message = encode_to_morse(message, shift)
    print("Encoded message:", final_message)
else:
    final_message = decode_from_morse(message, shift)
    print("Decoded message:", final_message)
    print("Shift used for decoding:", shift)
    
