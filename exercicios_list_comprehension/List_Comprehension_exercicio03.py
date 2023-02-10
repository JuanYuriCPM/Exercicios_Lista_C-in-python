"""#Count the number of spaces in the string 

string = "Practice Problems to Drill List Comprehension in Your Head." """

string = "Practice Problems to Drill List Comprehension in Your Head."
spaces = 0

list = len([
    i
    for i in string
    if i == ' '
])

print(list)