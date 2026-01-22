# write a pg to display a user entered name followed by good afternoon
Name=input("Enter your Name :")
print("Good Afternoon",Name)

#write a pg to hill in a letter template given below with name and data

Name =input("Enter your name :")
Date=input("Enter Date")

letter=f"Dear {Name},\n you are selected!\n{Date}" 
print(letter)

#write a pg to detect double spaces in string
# string="This is a   test String "
# print(string.find("  "))

# #replace double space with single space 
# string="This is a   test String "
# new_string=string.replace("  "," ")
# print(new_string)

# exercise 2 Greeting according to time 

import time 
timestamp = time.strftime("%H:%M:%S")
hour= int(time.strftime("%H"))
print(timestamp)

# timestamp=time.strftime("%H")
# print(timestamp)
# timestamp=time.strftime("%M")
# print(timestamp)
# timestamp=time.strftime("%S")
# print(timestamp)
if (hour>=0 and hour<12):
    print("Good Morning Sir")
elif(hour>=12 and hour<17):
    print("Good Afternoon sir")
elif(hour>=17 and hour<0):
    print("Good Night Sir")


