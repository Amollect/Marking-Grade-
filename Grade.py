#Read mark and provide grade

mark=float(input("enter percentage of student:"))
if mark>=75:
    print("***Distinction***")
elif (mark >=60 and mark <75):
    print("***1st Class***")
elif (mark >=50 and mark <60):
    print("***2nd Class***")
elif (mark >=40 and mark <50):
    print("***Pass Class***")
else:
     print("***failed***")