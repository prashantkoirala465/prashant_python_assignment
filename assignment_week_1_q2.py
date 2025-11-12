name = input("Please, enter your full name:")
name = name.strip()
parts = name.split()
first_letter = parts[0][0]
last_letter = parts[-1][0]
initials = first_letter.upper() + "." + last_letter.upper()
print("Your initials are: " + initials)