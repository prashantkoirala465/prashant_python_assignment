sentence = input("Enter a sentence: ")
words = sentence.split()
result_words = []
i = 0
while i < len(words):
    if i % 2 == 1:
        w = words[i]
        rev = ""
        j = 0
        while j < len(w):
            rev = w[j] + rev
            j = j + 1
        result_words.append(rev)
    else:
        result_words.append(words[i])
    i = i + 1
print(" ".join(result_words))
