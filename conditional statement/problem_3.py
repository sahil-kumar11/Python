marks1 = int(input("Enter the marks: "))
marks2 = int(input("Enter the marks: "))
marks3 = int(input("Enter the marks: "))

total_percentage = (100*(marks1 + marks2 + marks3)) / 300
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are eligible for the next semester")
else:
    print("You are not eligible for the next semester")