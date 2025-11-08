
roman_numerals = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

def to_roman(num):
    roman = ''
    for value in sorted(roman_numerals.values(), reverse=True):
        while num >= value:
            roman += list(roman_numerals.keys())[list(roman_numerals.values()).index(value)]
            num -= value
    return roman

def from_roman(roman):
    total = 0
    prev_value = 0
    for char in reversed(roman):
        value = roman_numerals.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

choice = input("Would you like to convert to Roman numerals or from Roman numerals? (t/f): ").strip().upper()
if choice not in ['T', 'F']:
    print("Invalid choice. Please enter 't' to convert to Roman numerals or 'f' to convert from Roman numerals.")
    exit()
if choice == 'T':
    number = int(input("Enter an integer to convert to Roman numerals: "))
    if number <= 0:
        print("Invalid number. Please enter a positive integer.")
        exit()
    roman_numeral = to_roman(number)
    print("Roman numeral:", roman_numeral)
else:
    roman_input = input("Enter a Roman numeral to convert to an integer: ").strip().upper()
    integer_value = from_roman(roman_input)
    if integer_value == 0:
        print("Invalid Roman numeral.")
        exit()
    print("Integer value:", integer_value)
    print("Roman numeral used for conversion:", roman_input)
    
    