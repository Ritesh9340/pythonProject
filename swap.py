A='Geeks for Geeks'
B='Learning from Geeks for Geeks'

C=A.split(' ')
D=B.split(' ')
e=[]
for i in D:
    if i  in C:
        continue
    else:
        e.append(i)
for i in C:
    if i  in D:
        continue
    else:
        e.append(i)
print(e)

# Function to find all close matches of
# input string in given list of possible strings
from difflib import get_close_matches

def closeMatches(patterns, word):
	print(get_close_matches(word, patterns))

# Driver program
if __name__ == "__main__":
	word = 'appel'
	patterns = ['ape', 'apple', 'peach', 'puppy']
	closeMatches(patterns, word)






