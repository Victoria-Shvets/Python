print("Enter a positive number:")
n = int(input())
if n > 0:
    for i in range(n):
        print('*' * (i+1))
else:
    print("You entered negative number or zero")