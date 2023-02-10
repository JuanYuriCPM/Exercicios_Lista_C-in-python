"""
Use a dictionary comprehension to count the length of each word in a sentence (use string above)

string = "Practice Problems to Drill List Comprehension in Your Head."
"""

string = "Practice Problems to Drill List Comprehension in Your Head."
words = string.split(" ")

dict = {
    word:len(word)
    for word in words
}

print(dict)