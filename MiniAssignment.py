from tabulate import tabulate
all_intakes = []

for i in range(1,6):
    Student_Name = input("Enter Student Name: ")
    Student_Admission = input("Enter Student Registration Number: ")
    Student_Age = int(input("Enter Student Age: "))
    English_Grade = int(input("Enter grades for English: "))
    Mathematics_Grade = int(input("Enter grades for Mathematics: "))
    Kiswahili_Grade = int(input("Enter grades for Kiswahili: "))

    Total = int(English_Grade + Mathematics_Grade + Kiswahili_Grade)
    Average = float(Total / 3)

    def Grade_Calculator():
        if (Average >0) and (Average < 40):
            Grade =  "F"
        elif (Average <=50):
            Grade =  "D"
        elif (Average <= 60):
            Grade = "C"
        elif (Average <=70):
            Grade = "B"
        elif (Average > 100) and (Average < 0):
            Grade = "Nullified"
        else:
            Grade = "A"
        return Grade

    def Classify_Grade():
        if Grade_Calculator() == "A":
            Status = "Distinction"
        elif Grade_Calculator() == "B":
            Status = "Credit"
        elif Grade_Calculator() == "C":
            Status = "Pass"
        elif Grade_Calculator() == "D":
            Status = "Fail"
        else:
            Status = "Fail"
        return Status

    student_list = [Student_Name, Student_Admission, Student_Age, Total, Average, Grade_Calculator(), Classify_Grade()]
    all_intakes.append(student_list)

print("\n--- Student Results ---")
print(tabulate([["Student Name", "Admission", "Age", "Total", "Average", "Grade", "Status"]] + all_intakes, headers="firstrow", tablefmt="grid"))
       