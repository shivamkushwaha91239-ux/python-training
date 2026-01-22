#read mode
 # open student.txt file in read mode and print its content
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

# # count the number of students in the file
# with open(r"C:\Users\Hp\Desktop\Student.txt","r") as file:
#     lines = file.readlines()
#     student_count = len(lines)
#     print("Number of students:", student_count)

# #write mode
# # open student.txt file in write mode and write 3 new student names
# with open(r"C:\Users\Hp\Desktop\Student.txt","w") as file:
#     file.write("Shivam\n")
#     file.write("Shobhit jhatu\n")
#     file.write("Aman\n")    

# #after writing open the file again and print its content
# with open(r"C:\Users\Hp\Desktop\Student.txt","r") as file:
#     content = file.read()
#     print("After Writing, File Content:\n",content)

#open products.txt file in read mode and display all products record
# with open(r"C:\Users\Hp\Desktop\Objects.txt","r") as file:
#     content = file.read()
# print("Products Record:\n",content)    

# # read and print only the first product from the file
# with open(r"C:\Users\Hp\Desktop\Objects.txt","r")as file:
#     first_product = file.readline()
#     print("First product :",first_product)

# #read all lines into a list and print the list
# with open(r"C:\Users\Hp\Desktop\Objects.txt","r") as file:
#     products = file.readlines()
#     print("All Products List:",products)    

# #read the line by line using a loop
# with open(r"C:\Users\Hp\Desktop\Objects.txt","r") as file:
#     for product in file:
#         print("product :",product)    
    
# #count the number of products in the file    
# with open(r"C:\Users\Hp\Desktop\Objects.txt","r") as file:
#     lines = file.readlines()
#     product_count=len(lines)
#     print("numbers of products : ",product_count)

# #display only the product name from the file
# with open(r"C:\Users\Hp\Desktop\Objects.txt","r") as file:
#     for line in file:
#         product_name = line.split(",")  
#         print("Product Name:", product_name[1]) 

# #display the products whose price is greater than 10000
# with open(r"C:\Users\Hp\Desktop\Objects.txt","r") as file:
#     for line in file:
#         product_name = line.split(",")
#         price = float(product_name[2])
#         if price >10000:
#             print("Expensive product :",product_name[1],"price :",price)        


# #write mode
# # open products.txt file in write mode and write the following products
# #P201, Headphones, 2000,Electronics
# #P202,Sofa,28000,Furniture
# #P203,Printer,12000,Electronics

# with open(r"C:\Users\Hp\Desktop\Objects.txt","w") as file:
#     file.write("P201,Headphones,2000,Electronics\n")
#     file.write("P202,Sofa,28000,Furniture\n")
#     file.write("P203,Printer,12000,Electronics\n")
# print("Products written to the file successfully.")  

# # After writing ,reopen the file again and display its content
# with open(r"C:\Users\Hp\Desktop\Objects.txt","r") as file:
#     content = file.read()
#     print("After Writing, File Content:\n",content)

# # append mode
# # open the file in append mode and add the product P204,fan,3500,Electronics

# with open(r"C:\Users\Hp\Desktop\Objects.txt","a") as file:
#     file.write("P204,fan,3500,Electronics\n")
# print("Product appended to the file successfully.")

# #verify that the new product is added at the end of the file 
# with open(r"C:\Users\Hp\Desktop\Objects.txt","r") as file:
#     content = file.read()
#     print("After Appending, File Content:\n",content)

# #read and write mode
# # 
# # open the file r+ mode and update the product name "headphone "to wireless headphone

# with open(r"C:\Users\Hp\Desktop\Objects.txt","r+") as file:
#     content = file.read()
#     content = content.replace("Headphones","Wireless Headphones")
#     file.seek(0)
#     file.write(content)

# #using r+ mode ,move the cursor to the end of the file and add
# # the product P205,Bed,45000,Furniture
# with open(r"C:\Users\Hp\Desktop\Objects.txt","r+") as file:
#     file.seek(0,2) # move the cursor to the end of the file
#     file.write("P205,Bed,45000,Furniture\n")

# #logical Thinking
# # 
# # Count how many products belong to the Electronics category    
# with open(r"C:\Users\Hp\Desktop\Objects.txt","r") as file:
#     electronics_count = 0
#     for line in file:
#         product_details = line.split(",")
#         category = product_details[3].strip()
#         if category == "Electronics":
#             electronics_count += 1
#     print("Number of Electronics products:", electronics_count)


#create a new file expensive_products.txt and write only those products whose price is greater than 20000

with open(r"C:\Users\Hp\Desktop\Objects.txt","r") as file:
    with open(r"C:\Users\Hp\Desktop\expensive_products.txt","w") as expensive_file:
        for line in file:
            product_details = line.split(",")
            price = float(product_details[2])
            if price > 20000:
                expensive_file.write(line)   
file.close()
              