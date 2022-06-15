string = 'A'
number = (int(input("Enter number of rows: ")))
for i in range(number):
    for j in range(i+1):
        print(string, end="")
        if string == 'Z':
            string = 'A'
        else:
            string = chr(ord(string) + 1)
    print()