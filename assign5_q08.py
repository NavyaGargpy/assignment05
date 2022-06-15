a = int(input("enter integer 1 : "))
b = int(input("enter integer 2 : "))
c = int(input("enter integer 3 : "))
d = int(input("enter integer 4 : "))
e = int(input("enter integer 5 : "))
f = int(input("enter integer 6 : "))
g = int(input("enter integer 7 : "))
h = int(input("enter integer 8 : "))
i = int(input("enter integer 9 : "))
j = int(input("enter integer 10 : "))

li = [a,b,c,d,e,f,g,h,i,j]

print("positive numbers are: ")
for number in li:
    if number>=0:
        print (number,"  ",end="")
    

print("")
print("negative numbers are: ")
for number in li:
    if number<0:
        print (number,"  ",end="")
    

print("")
print("odd numbers are: ")
for number in li:
    if number%2 != 0:
        print (number,"  ",end="")


print("")
print("even numbers are: ")
for number in li:
    if number%2 == 0:
        print (number,"  ",end="")


print("")
li_set = set(li)
for number in li_set:
    print("number of times ",number," comes in list is ",li.count(number))
    
