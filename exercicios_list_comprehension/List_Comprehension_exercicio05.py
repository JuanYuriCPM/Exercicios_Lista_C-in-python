"""
Find all of the words in a string that are less than 5 letters (use string above)

string = "Practice Problems to Drill List Comprehension in Your Head."
"""

string = "Practice Problems to Drill List Comprehension in Your Head."

words = string.split(' ')

list = [
    i
    for i in words
    if len(i) < 5
]

print(list)
print(words)