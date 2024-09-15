print("Objective : To check whether a positive number is prime number")
a = int(input("Enter the number : "))
p = 1

if(a<0):
   print("Please enter a positive number") 
   
elif(a<2 and a>0 ):  #As no prime numbers present in that domain
   print(f"{a} is not a prime number")

elif(a==2):
   print(f"{a} is a prime number")

elif(a>2):
   for i in range(2,a):
      if(a%i == 0):
         p +=1     
      break

if(p>1):
   print(f"{a} is not a prime number")
else:
   print(f"{a} is a prime number")




    