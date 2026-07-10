s= input("Enter the word: ").lower()

vowel="aeiou"

is_vowel= any(char in s for char in vowel )

print(f"Vowel presence in string is {is_vowel}")