square = lambda x: x*x

y = int(input("Enter a number : "))
print(f"The sqaure of {y} is {square(y)}")


avg = lambda a,b,c,d: (a+b+c+d)/4

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))
d = int(input("Enter a number : "))

print(f"The average of given numbers is {avg(a,b,c,d)}")