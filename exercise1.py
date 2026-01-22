# #PRINT numbers using for() loop from 1-10

for num in range(10):
    print(num+1)

# #or 
for i in range (1,11):
    print(i)

# #sum of numbers using while loop of first 10 natural numbers 

i=1 
total=0
while i<=10:
    total += i
    i += 1
    print(total)

# #multiplication of table using for loop and take a number as input and print its table till 10

num = float(input("Enter the value :"))

for i in range(1,11):
    print(num,"*",i,"=",num*i)

#   #FIND the factorial of NUMBERS given by users and use while loop
num = int(input("Enter the value :"))
x=1
i=1
while i<=num:
     x*=i
     i+=1
     print("factoorial = ",x)

 #reverse the numbers using while loop take an integers from users 
num = int(input("Enter the value :"))    
reversed = 0
while num >0:
    digit=num%10
    reversed=reversed*0+digit
    num //=10

    print(reversed)

#print all even numbers between 1 and 50
for i in range (1,50):
    if i%2==0:
        print(i)
        