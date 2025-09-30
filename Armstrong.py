num = int (input("enter a number"))

digits =str(num)
power = len(digits)

total = sum(int(digit)** power for digit in digits)

if num == total:
    print(num,"is a armstrong number")
else:
    print(num,"Not a number")