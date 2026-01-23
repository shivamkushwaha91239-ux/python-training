#math module
# find the square root of a 625
import math
num=625
Square_root=math.sqrt(num)
print("the square root of:",num,"is",Square_root)

#claculate the factorial of 6

num=6
factorial=math.factorial(num)
print("the factorial of:",num,"is",factorial)

#compute 5 raised to the power 3 the math module

base=5
exponent=3
power= math.pow(base,exponent)
print("the value of",base,"raised to the power",exponent,"is",power)

#find the absolute value of -18 using math.fabs()

num=-18
absolute_value=math.fabs(num)
print("the absolute value of:",num,"is",absolute_value)

#find the sine ,cosine,and tangent of 90 degress (convert degrees to radians)
print(math.sin(math.radians(90))) 
print(math.sin(math.degrees(1))) 
print(math.cos(math.radians(90))) 
print(math.tan(math.radians(90)))
 

#find the greatest common divisor (GCD) of 36 and 60

num1=36
num2=60
gcd=math.gcd(num1,num2)
print("the greatest common divisor of",num1,"and",num2,"is",gcd)

#find the value of e3 using math module
#we using math.exp() function

exponent=3  
exponential_value=math.exp(exponent)
print("the value of e raised to the power",exponent,"is",exponential_value)


#find the logarithm base 10 of 1000 using math module

num=1000
log_value=math.log10(num)
print("the logarithm base 10 of ",num,"is",log_value)

#convert 180 degrees into radians

degress=180
radians=math.radians(degress)
print("the value of",degress,"degrees in radians is",radians)   