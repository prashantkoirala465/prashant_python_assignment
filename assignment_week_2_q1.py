nums_input = input("Enter numbers separated by space: ")
parts = nums_input.split()
nums = []
for p in parts:
    if p.isdigit():
        nums.append(int(p))
    elif p.startswith('-') and p[1:].isdigit():
        nums.append(int(p))
for n in nums:
    if n > 50:
        break
    if n % 5 == 0:
        continue
    print(n)