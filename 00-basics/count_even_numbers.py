# Problem: Count even numbers in a list
# Difficulty: Easy

nums = [1, 2, 3, 4, 6]

count = 0

for n in nums:
    if(n % 2 == 0):
        count += 1

print(f"There are total {count} even numbers in the list.")