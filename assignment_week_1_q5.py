text = input("Please, enter a string: ")
text = text.lower()
frequency = {}
for char in text:
    if char.isalpha():
        if char in frequency:
            frequency[char] = frequency[char] + 1
        else:
            frequency[char] = 1
for char, count in frequency.items():
    print(char, "→", count)