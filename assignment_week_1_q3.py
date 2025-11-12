word = input("Please, enter a word:")
print("Enter starting index:")
index = input()
index = int(index)
substring = word[index:]
print('Substring from index', index, ':', '"' + substring + '"')