"""
Python List append() Method – Practice Programs
Author: Omkar Mane
Description: Examples demonstrating different uses of the list.append() method
"""

# 1. Append different data types to a list
my_list = [1, 2, 3]

my_list.append(5)          # Append integer
my_list.append("omkar")    # Append string
my_list.append(3.14)       # Append float
my_list.append(True)       # Append boolean

print("Mixed data list:", my_list)


# 2. Append multiple values using loop
numbers = []
for i in range(1, 8):
    numbers.append(i)
print("Numbers list:", numbers)


# 3. Append elements from another list
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

for i in b:
    a.append(i)
print("Merged list:", a)


# 4. Append a list inside another list
a = [1, 2, 3, 4]
b = [7, 8, 9]

a.append(b)
print("Nested list:", a)


# 5. Append characters of a string
letters = []
for ch in "OMKAR":
    letters.append(ch)
print("Characters list:", letters)


# 6. Append length of each string
words = ["hi", "hello", "python"]
lengths = []

for w in words:
    lengths.append(len(w))
print("Word lengths:", lengths)


# 7. Append user-entered numbers (optional)
# nums = []
# for i in range(3):
#     nums.append(int(input("Enter number: ")))
# print(nums)