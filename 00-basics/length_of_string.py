# Problem: Find length of a string (without using len())
# Difficulty: Easy


def length_of_string(word):
    count = 0
    for ch in word:
        count += 1
    return count

word = input("Enter string: ")
result = length_of_string(word)
print(result)



