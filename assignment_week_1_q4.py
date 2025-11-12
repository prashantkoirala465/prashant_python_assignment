password = input("Please, enter your password:")
if len(password) < 6 or password.isalpha():
    print("Password strength: Weak")
elif len(password) >= 6 and password.isalnum():
    print("Password strength: Moderate")
elif len(password) >= 8 and any(c in "@#$%&" for c in password):
    print("Password strength: Strong")
else:
    print("Password strength: Moderate")