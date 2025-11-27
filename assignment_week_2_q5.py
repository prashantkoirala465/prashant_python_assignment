inp = input("Enter words separated by space: ")
items = inp.split()
freq = {}
for w in items:
    lw = w.lower()
    if lw in freq:
        freq[lw] = freq[lw] + 1
    else:
        freq[lw] = 1
print(freq)
