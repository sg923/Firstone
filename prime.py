# Program to check if a number is prime or not

n = 407

# To take input from the user
#num = int(input("Enter a number: "))

# prime numbers are greater than 1
if n > 1:
   # check for factors
   for i in range(2,n):
       if (n % i) == 0:
           print(n,"is not a prime number")
           print(i,"times",n//i,"is",n)
           break
   else:
       print(n,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(n,"is not a prime number")

   print("Yo!man how are you")
   print("Hi hello")
