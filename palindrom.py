def check_pd(x):
    x=str(x)
    flag=False
    if len(x)>0:
        for i in range(0,int(len(x)/2)):
            if x[i] == x[(-i-1)]:
                flag=True
            else:
                flag=False
        if flag:
             print("it's palindrome")
        else:
            print(("it's not palindrome"))
    else:
        print("kindly  provide input")

check_pd('abcdedca')


