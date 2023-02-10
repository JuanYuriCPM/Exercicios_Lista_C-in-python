"""Remove all of the vowels in a string (use string above)

string = "Practice Problems to Drill List Comprehension in Your Head."""

string = "Practice Problems to Drill List Comprehension in Your Head."

vowels = ['a', 'e', 'i', 'o', 'u']

list = [
    i
    for i in string
    if i.lower() not in vowels
]

print(list)