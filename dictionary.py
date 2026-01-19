# Student={
#     "name": "Shivam",
#     "age": 21,
#     "courses": ["Math", "Computer Science", "Art", "History", "Biology"],
#     "address": {
#         "street": "Tiwari Ganj utthardhona",
#         "city": "lucknow",
#         "state": "UP",
#         "zip": "226028"
#     }
# }
# print(Student.get("email"))
# print(Student["name"])
# print(Student["age"])   
# print(Student["courses"])
# print(Student["address"]["city"])
# Student["phone"]="9120379339"
# print(Student)



#create a dictionary of 5 countries and their capitals .print 
countries_capitals={
    "India":"New Delhi",
    "USA":"Washington D.C.",
    "France":"Paris",
    "Germany":"Berlin",
    "Japan":"Tokyo"
}
print(countries_capitals)
# #access the capital of india from dictionary
# print("Capital of India :",countries_capitals["India"])

# #add a new key value pair nepal:katmandu to dictionary
# countries_capitals["nepal"]="Katmandu"
# print(countries_capitals)           

# #updATE the capital of USA FROM washington D.C TO NEW YORK
# countries_capitals["USA"]="New York"
# print(countries_capitals)

# #delete the key value pair of germany using del keyword
# del countries_capitals["Germany"]   
# print(countries_capitals)

#create a dictionary of of students and their marks.using keys() to print all students 
students_marks={
    "Shivam":85,
    "Aman":90,
    "Rishi":78,
    "Abhishek":88,
    "Amandeep":92
}           
for student in students_marks.keys():
    print("Student Name:",student)  

    

#copying
#create a dictionary,make a copy using .copy() and update the copy without affecting original dictionary
original_dict={"Sanoj":23,"Abhishek":45,"Rishi":34}
copied_dict=original_dict.copy()
copied_dict["Amandeep"]=48
print("Original Dictionary:",original_dict)
print("Copied Dictionary:",copied_dict)