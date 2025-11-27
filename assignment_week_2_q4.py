books = {
    'Book1': 5,
    'Book2': 6,
    'Book3': 10
}
name = input("Enter the name of the book you want: ").strip()
while True:
    copies_str = input("Enter number of copies to buy: ").strip()
    if copies_str.isdigit():
        copies_req = int(copies_str)
        break
    else:
        print("Invalid input. Please enter a valid integer number of copies.")
if name in books:
    available = books[name]
    if available >= copies_req:
        print("Available")
    elif available > 0 and available < copies_req:
        print("Partially Available")
    else:
        print("Unavailable")
else:
    print("Unavailable")
