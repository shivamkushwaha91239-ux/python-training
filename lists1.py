
# #create a list of five numbers .print the first element ,last element,and length of list 

# numbers=[10,20,30,40,50,60,70,80]
# print("First Element :",numbers[0])
# print("last Element :",numbers[-1])
# print("Length of Numbers",len(numbers))

# #take a list of numbers and find the sum and average using built in functions

# num_1=[4,5,45,34,23,5]
# TotalSum=sum(num_1)
# average=TotalSum/len(num_1)
# print("sum :",TotalSum)
# print("average :",average)

# #create a list of fruits .add a new fruit using append and insert one at position 2 using insert()

# fruits= ["apple","banana","cherry"]
# fruits.append("orange")
# fruits.insert(2,"grapes")
# print("fruits list",fruits)

# # remove an element from list using remove()and delete the last element using pop()
# fruits= ["apple","banana","cherry"]
# fruits.remove("banana")
# fruits.pop()
# print("updated list",fruits)

# #create a list with duplicate numbers .use count() to check how many times a numbers appear

# dup_num=[1,2,4,2,5,6,7,2,6,6]
# count_of_twos=dup_num.count(2)
# print("Count of numbers 2:",count_of_twos)


# create a pg to displaying question like to the user like kbc use list to store the questions and their correct answers display the final amount the person is taking home after playing the game
Questions =[ ["Capital of Bihar?", "A. Mumbai", "B. Patna", "C. West Champaran", "B", 700],
    ["5 + 7 = ?", "A. 12", "B. 10", "C. 11", "A", 800],
["Founder of Python?","A.Guido Van Rossum","B.James gosling","C.Sarfraz","A",2000]]
total_amount=0

print("Welcome to the Quiz Game!\n")

for q in Questions:
    print(q[0])
    print(q[1])
    print(q[2])
    print(q[3])

    Answer = input("Enter your answer (A/B/C):").strip().upper()

    if Answer == q[4]:
        print(" Awsome !Correct Answer you won Rs.",q[5],"\n")
        total_amount +=q[5]
    else:
        print("Ohh! Wrong answer Correct Answer is ",q[4])

        print("Game is over! \n")
        break
    print("Final amount you can Take to your home : Rs.",total_amount)