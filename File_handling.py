#read mode
# # # open student.txt file in read mode and print its content
# with open(r"C:\Users\Hp\Desktop\Student.txt","r") as file:
#     content = file.read()
#     print(content)

# #read only the first line of the file
# with open(r"C:\Users\Hp\Desktop\Student.txt","r") as file:
#     content = file.readline() # for first line
#     print("First Line:",content)

# # read all lines into a list and print them
# with open(r"C:\Users\Hp\Desktop\Student.txt","r") as file:
#     content = file.readlines() # for all lines
#     print("All Lines:",content)

# # loop through the file and print each line separately
# with open(r"C:\Users\Hp\Desktop\Student.txt","r") as file:
#     for line in file:
#         print("Line:",line)

# count the number of students in the file
with open(r"C:\Users\Hp\Desktop\Student.txt","r") as file:
    lines = file.readlines()
    student_count = len(lines)
    print("Number of students:", student_count)