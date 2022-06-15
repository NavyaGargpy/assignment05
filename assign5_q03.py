a = float(input("enter side 1 : "))          # asks user for the three sides
b = float(input("enter side 2 : "))
c = float(input("enter side 3 : "))

statement = True
if a+b>c and b+c>a and a+c>b:
    statement = True
    print("given combination of sides is possible")
else:
    statement = False
    print("given combination of sides is not possible")

s = (a+b+c)/2               #half perimeter of triangle

x = s - a
y = s - b                    #heron's formula says area = (s*(s-a)*(s-b)*(s-c))**(1/2)
z = s - c

area = (s*x*y*z)**(1/2)
if statement == True :
    print("area of triangle is " , area )



