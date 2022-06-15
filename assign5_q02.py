number = int(input("enter number: "))      #asks user for a number and the range
range_start = int(input("enter starting number of range : "))
range_end = int(input("enter ending number of range : "))      

for i in range(range_start,range_end+1):            
    if i%number == 0:
        print(i)
