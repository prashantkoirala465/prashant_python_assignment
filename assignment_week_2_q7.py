def to_title_case(sentence):
    words = sentence.split()
    titled = []
    for w in words:
        if w == "":
            titled.append(w)
            continue
        neww = ""
        i = 0
        while i < len(w):
            ch = w[i]
            if i == 0:
                neww = neww + ch.upper()
            else:
                neww = neww + ch.lower()
            i = i + 1
        titled.append(neww)
    return " ".join(titled)

s = input("Enter a sentence: ")
print(to_title_case(s))
