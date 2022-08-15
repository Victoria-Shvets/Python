print("Enter number:")
n = int(input())
i = 0
if n > 0:
    while i < n:
        print('*' * (i + 1))
        i = i + 1
else:
    print("You entered negative number")