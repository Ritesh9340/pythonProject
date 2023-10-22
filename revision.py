def check(x):
    falg=False  # Initialize the flag as False
    if x > 1:
        for i in range(2, x):
            if (x % i == 0):
                falg = True

    if not falg:  # Correct the condition
        print("It's a prime number")
    else:
        print("It's not a prime number")

check(3)
