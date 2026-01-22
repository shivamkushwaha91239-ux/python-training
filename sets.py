# # create a set of 5 colors and print it
# colors ={'red','orange','purple','blue',"green"}
# print(colors)

# #creates a set of numbers with duplicates and check how pythin handles duplicates

# my_num={1,1,3,2,5,4,6,7,2}
# print(my_num)

# #write a program to loop through a set and and print each element
# colors ={'red','orange','purple','blue',"green"}
# for color in colors:
#     print(colors)

#  # create a set and use .add()to insert a new element

# colors ={'red','orange','purple','blue',"green"}   
# add=colors.add("yellow")
# print(add)


# #remove an element using .remove and observe what happens if element is not

# colors ={'red','orange','purple','blue',"green"}
# discard=colors.discard("yellow")

# remove=colors.remove("yellow")
# print(discard)
# print(remove)

# #us e.pop to remove random value
# colors ={'red','orange','purple','blue',"green"}
# pop=colors.pop()
# print(pop)

#create a set and find their union,intersection,difference

a={1,2,3,4}
b={3,4,5,6}
union=a.union(b)
intersection=a.intersection(b)
difference=a.difference(b)
print(union)
print(intersection)
print(difference)

# weite a pg to find all unique charcters in string using set
input_string={"Hello world"}
unique_charcters = set(input_string)
print("unique cahrcters:",unique_charcters)

#givw=en a two list of students (cricket and football),find who play both sports

cricket={'alice','aman','abhishek','shivam'}

football={'alice','aman','rishi','amandeep'}
both_sports=cricket.union(football)
print(both_sports)