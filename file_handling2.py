file= open(r"C:\Users\Hp\Desktop\studentsmarks.txt","r") 
i=0
while True:
 i=i+1
 line=file.readline()
 if not line:
   break
 m1=int(line.split(",")[0])
 m2=int(line.split(",")[1]) 
 m3=int(line.split(",")[2])

 print(f"Marks of student {i} in maths  is {m1}")
 print(f"Marks of student {i} in Science is {m2}")
 print(f"Marks of student {i} in SST is {m3}")

 print(line)