print("Please, enter a string:")
text = input()
text = text.lower()
vowels = "aeiou"
vowel_count = 0
consonant_count = 0
for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count = vowel_count + 1
        else:
            consonant_count = consonant_count + 1
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)