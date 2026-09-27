Students = 5
for i in range(Students):
    print(f"\nEnter the next student's grades for Student {i + 1}:")
StudentName = (input("Enter Student Name: "))
English = int(input("Enter grades for English: "))
Mathematics = int(input("Enter grades for Mathematics:"))
Science = int(input("Enter grades for Science: "))

Total = (English+Mathematics+Science)
Average = Total/3

if Average >=40 and Average<50:
    Grade = "D"
elif Average >=50 and Average <60:
    Grade = "C"
elif Average >=60 and Average <70:
    Grade = "B"
elif Average >=70:
    Grade = "A"
else :
    Grade = "F"

    print("\n--- Student Result ---")
    print("Name:", StudentName)
    print("Total Marks:", Total)
    print("Average Marks:", round(Average, 2))
    print("Grade:", Grade)