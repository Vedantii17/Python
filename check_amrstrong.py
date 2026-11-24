n = 153
total = 0

for digit in str(n):
    total += int(digit) ** len(str(n))

if total == n:
    print("Armstrong Number")
else:
    print("Not Armstrong")