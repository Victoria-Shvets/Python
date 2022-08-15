print("Enter value of minutes!")
minutes = int(input())

if 0 <= minutes <= 15:
    print(f"{minutes} lays in the first quarter!")
elif 16 <= minutes <= 30:
    print(f"{minutes} lays in the second quarter!")
elif 31 <= minutes <= 45:
    print(f"{minutes} lays in the third quarter!")
elif 46 <= minutes <= 60:
    print(f"{minutes} lays in the fourth quarter!")
elif minutes > 60:
    if 0 <= minutes % 60 <= 15:
        print(f"{minutes} lays in the first quarter!")
    elif 16 <= minutes % 60 <= 30:
        print(f"{minutes} lays in the second quarter!")
    elif 31 <= minutes % 60  <= 45:
        print(f"{minutes} lays in the third quarter!")
    elif 46 <= minutes % 60 <= 60:
        print(f"{minutes} lays in the fourth quarter!")
else:
    print("Warning! Enter a valid number!")