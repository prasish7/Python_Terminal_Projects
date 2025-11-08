
word = input("Enter a word: ")
isRunning = True
while isRunning:
    print("Select an option:")
    print("1. Count vowels")
    print("2. Count consonants")
    print("3. Count total letters")
    print("4. Exit")
    choice = int(input("Enter the number of your choice (1-4): "))
    
    if choice == 1:
        vowels = "aeiouAEIOU"
        vowel_count = 0
        for char in word:
            if char in vowels:
                vowel_count += 1
        print(f"The word '{word}' has {vowel_count} vowels.")
        
    elif choice == 2:
        vowels = "aeiouAEIOU"
        consonant_count = sum(1 for char in word if char.isalpha() and char not in vowels)
        print(f"The word '{word}' has {consonant_count} consonants.")
        
    elif choice == 3:
        letter_count = sum(1 for char in word if char.isalpha())
        print(f"The word '{word}' has a total of {letter_count} letters.")
        
    elif choice == 4:
        print("Exiting the program.")
        isRunning = False
        
    else:
        print("Invalid choice. Please select a number between 1 and 4.")