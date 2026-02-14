#set-1
#question-1
#even numbers using while loop

start=int(input("Enter start value:"))
end=int(input("Enter end value:"))

while end>=start:
    if start%2==0:
        print(start,end=" ")
    start+=1

# OUTPUT:
# Enter start value:2
# Enter end value:20
# 2 4 6 8 10 12 14 16 18 20  

#question-2
#Write a Python program that asks the user for a number and keeps asking until the user enters a number greater than 10. Print the number once it is greater than 10

while True:
    n=int(input("Enter a number:"))
    if n>10:
        print(n)
        break

# OUTPUT:
# Enter a number:3
# Enter a number:4
# Enter a number:5
# Enter a number:6
# Enter a number:7
# Enter a number:12
# 12

#question-3
#Write a Python program to sum all the numbers entered by the user until the user enters a negative number. The program should then display the total sum.

sum=0
while True:
    n=int(input("Enter a number:"))
    if n<0:
        print("You have enter -ve value...")
        break
    else:
        sum+=n
print(sum)

# OUTPUT:
# Enter a number:34
# Enter a number:66
# Enter a number:-1
# You have enter -ve value...
# 100

#set-2
#question-1
# Write a Python program that prompts the user to input a number and prints whether the number is even or odd. Use a while loop to keep asking the user for input until they enter a negative number.


while True:
    n=int(input("Enter a number:"))
    if n<0:
        print("You have enter -ve value...")
        break
    else:
        if n&1:  #value 0 so false so odd / n&1==0 is true so even
            print("Odd")
        else:
            print("Even")

# OUTPUT:
# Enter a number:23
# Odd
# Enter a number:21
# Odd
# Enter a number:22
# Even
# Enter a number:-1
# You have enter -ve value...

#question-2
# Write a program using a while loop that calculates and prints the factorial of a number provided by the user. The user should input the number, and the loop should calculate the factorial.

n=int(input("Enter a number:"))
fact=1
temp=n
while n>0:
    fact*=n
    n-=1
print(f"Factorial of {temp} is {fact}")

# OUTPUT:
# Enter a number:4
# Factorial of 4 is 24

# question-3
# Create a Python program that asks the user for a number and prints a countdown from that number to 0 using a while loop. Once it reaches 0, print "Blastoff!"

n=int(input("Enter a number:"))

while n>0:
    print(f"Counrdown:{n}")
    n-=1
print("Blast off")

# OUTPUT:
# Counrdown:3
# Counrdown:2
# Counrdown:1
# Blast off

#set-3
#question-1
# Write a Python program that accepts a number from the user and uses a while loop to calculate and print the sum of all integers from 1 to that number. 

n=int(input("Enter a number:"))
sum=0
temp=n
while n>=1:
    sum+=n
    n-=1
print(f"Sum of integers from 1 to {temp} is {sum}")

# OUTPUT:
# Enter a number:4
# Sum of integers from 1 to 4 is 10

#question-2
# Write a Python program using a while loop that takes input from the user and continues to ask for numbers until the user enters the number 0. Once 0 is entered, print the sum of all the numbers entered.

sum=0
while True:
    n=int(input("Enter a number:"))
    if n==0:
        print("You have entered 0 ...")
        break
    else:
        sum+=n
print(sum)

# OUTPUT:
# Enter a number:34
# Enter a number:32
# Enter a number:66
# Enter a number:0
# You have entered 0 ...
# 132

# question-3
# Write a Python program that uses a while loop to print the Fibonacci sequence up to the nth term, where n is provided by the user.

n=int(input("Enter a number:"))

a,b=0,1

if n<0:
    print(a)
elif n==1:
    print(a,b)
else:
    while n>=0:
        print(a,end=" ")
        a,b=b,a+b
        n-=1

#OUTPUT:
# Enter a number:5
# 0 1 1 2 3 5 