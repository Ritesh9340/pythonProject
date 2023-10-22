a='Geeks123For1239Geeks'
b=['1','2','3','4','5']
c=''
for i in a:
    if i not in b:
        c+=i
    else:
        continue
print(c)

# Python program to illustrate use of exec to
# execute a given code as string.

# function illustrating how exec() functions.
code = '"hello" + "world"'
result = eval(code)
print(result) # Output: "hello world"

code = '["a", "b", "c"][1]'
result = eval(code)
print(result) # Output: "b"


