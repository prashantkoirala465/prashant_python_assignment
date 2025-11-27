inp = input("Enter words separated by space: ")
items = inp.split()
freq = {}
for w in items:
    if w in freq:
        freq[w] = freq[w] + 1
    else:
        freq[w] = 1
duplicates = {}
for k in freq:
    if freq[k] > 1:
        duplicates[k] = freq[k]
print(duplicates)
