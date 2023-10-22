def myfunc(s):
    a=''
    b=''
    for i in range(int(len(s)/2)):
        a+=s[i]
    for j in range(int(len(s)/2),int(len(s))):
        b+=s[j]
    if a==b:
        print('string is symatric')
    else:
        print('string is not sysmatric')
myfunc('abcsfj jfgerre')

# code
string ="malayalam"
print("the string is palindrome" if string==reversed(string) else "the string is not palindrome")


