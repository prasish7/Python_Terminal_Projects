from string import ascii_lowercase, ascii_uppercase

choice = input("Would you like to encode or decode a message? (e/d): ").strip().upper()
if choice not in ['E', 'D']:
    print("Invalid choice. Please enter 'e' to encode or 'd' to decode.")
    exit()
    
message = input("Enter your message: ")
shift = int(input("Enter the shift number (1-25): "))

if shift < 1 or shift > 25:
    print("Invalid shift number. Please enter a number between 1 and 25.")
    exit()

if choice == 'D':
    shift = -shift
    
result = []

for char in message:
    if char in ascii_lowercase:
        index = ascii_lowercase.index(char)
        new_index = (index + shift) % 26
        result.append(ascii_lowercase[new_index])
    elif char in ascii_uppercase:
        index = ascii_uppercase.index(char)
        new_index = (index + shift) % 26
        result.append(ascii_uppercase[new_index])
    else:
        result.append(char)

final_message = ''.join(result)
if choice == 'E':
    print("Encoded message:", final_message)    
else:
    print("Decoded message:", final_message)
    print("Shift used for decoding:", -shift)
  
    


