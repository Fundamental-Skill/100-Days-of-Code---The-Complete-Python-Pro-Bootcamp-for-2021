# Write your code below this row 👇

total = 0
total2 = 0

# Solution 1
for i in range(1, 101):
    if i % 2 == 0:
        total += i

# Solution 2
for i in range(2, 101, 2):
    total2 += i

print(total)
print(total2)
