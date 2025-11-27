def largest_word(sentence):
    words = sentence.split()
    if len(words) == 0:
        return ""
    longest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest

s = input("Enter a sentence: ")
print(largest_word(s))
