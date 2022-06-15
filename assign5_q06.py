s_range = int(input("enter a starting range : ") )
e_range = int(input("enter a ending range : "))

for number in range(s_range,e_range+1):
    i = 2
    while i <=number:
        if number%i == 0:
            break
        i = i + 1
    
    if  i == number :
        print(number)
    else:
        print("",end="")



