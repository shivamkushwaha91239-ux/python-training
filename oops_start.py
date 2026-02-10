# class person:
#     Name = "Shivam"
#     Age = 25
#     city = "Lucknow"
#     occupation = "Engineer"

#     def info(self):
#         print(f"The person's name is {self.Name} and his age is {self.Age}.He lives in {self.city} and works as a\an {self.occupation}.")

# a = person()
# b = person() 
# c = person() 

# a.Name = "Rahul"
# a.Age = 30
# a.city = "Delhi"
# a.occupation = "Doctor"

# b.Name = "Anjali"
# b.Age = 23
# b.city = "Mumbai"
# b.occupation = "Artist"

# a.info()
# b.info()
# c.info()   # picks default value if value is not passed 

# we can create above code in better way using construrcor

class person:
    def __init__(self, name, age, city, occupation):
        #"Constructor called"
        self.name = name
        self.age = age
        self.city = city
        self.occupation = occupation

    def info(self):
        print(f"The person's name is {self.name} and his age is {self.age}.He lives in {self.city} and works as a\an {self.occupation}.")


a = person("Rahul",30,"Delhi","Doctor")
b = person("Anjali",23,"Mumbai","Artist")
c = person("Shivam",25,"Lucknow","Engineer")

a.info()
b.info()
c.info
