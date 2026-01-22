# # write a program to print fabonacci sequence in for loop
# def fibonacci(n):
#     fib_sequence = [0,1]
#     for i in range (2,n):
#         next_fib = fib_sequence[i-1] + fib_sequence[i-2]
#         fib_sequence.append(next_fib)
#         return fib_sequence[:n]     

#     print(fibonacci(10))


# def greet():
#     print("Hello! Welcome to the program.")
# greet()
 
#  # write a function to print Hello ,world
# def hello_world():
#    print("Hello,World!")

# hello_world()

# #write a function that takes a name as input and prints "Hello,<name>!"
# def greet_user(name="guest"):
#     print("Hello!",name)
# greet_user()
# greet_user("Shivam")

# #write a function that takes two numbers and print their sum
# def add(a,b):
#     return a+b
# sum=add(4,5)
# print("sum =",sum)

# # write a function that returns the square of a number
# num = int(input("Enter a number to find its square: "))
# def square(num):
#     return num*num
# result = square(num)
# print("Square =",result)

#write a function to check if a number is even or odd
# n
# write a function that takes two numbers and their  maximum
a = int(input("Enter first number: "))
b = int(input("Enter second number: ")) 
def maximum(a,b):
     if a>b:
         return a
     else:
        return b
print("Maximum =",maximum(a,b))
    #write a function
    #  that takes a list of numbers and returns their average
# def average(numbers):
#         total=sum(numbers)
#         avg=total/len(numbers)
#         return avg
# num_list=[4,5,6,7,8]
# result=average(num_list)
# print("Average =",result)

 # write a function that counts the vowels in a string
# def count_vowels(input_string):
#         vowels = "aeiouAEIOU"
#         count = 0
#         for char in input_string:
#             if char in vowels:
#                 count +=1
#         return count
# string = input("Enter a string to count vowels: ")
# vowel_count = count_vowels(string)  
# print("Number of vowels:",vowel_count)

#write a function to find the factorial of a number using loop

# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
# n = int(input("Enter a number to find its factorial: "))
# print("Factorial =",factorial(n))
# #Write a function to check if a string is a palindrome
# s = input("Enter a string :")

# if s == s[::-1]:
#     print("The string is a palindrome.",s)
# else:
#     print("The string is not a palindrome.",s)

  #Write a function that calculates simple interest (default rate = 5%)
  # Simple Interest = (Principal * Rate * Time) / 100
def SI(principal,time,rate=5):
    si=(principal*rate*time)/100
    return si
principal=float(input("Enter Principal amount: "))
time=float(input("Enter Time in years: "))
r=float(input("Enter Rate of interest: "))
print("Simple Interest is:",SI(principal,time,r))

