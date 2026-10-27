


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate marks (%): "))

    subjects = int(input("Enter number of subjects: "))
    marks = []

    for j in range(subjects):
        mark = float(input(f"Enter marks in subject {j + 1}: "))
        marks.append(mark)

    attendance = float(input("Enter attendance (%): "))
    income = float(input("Enter annual family income: "))

    
    if (aggregate >= 75 and
        all(mark >= 60 for mark in marks) and
        attendance >= 75 and
        income <= 250000):

        students.append({
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

        print(name, "is Eligible for Scholarship")

    else:
        print(name, "is Not Eligible for Scholarship")



students.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["attendance"],
        x["income"]
    )
)


print("\n===== SCHOLARSHIP RANK LIST =====")

if students:
    for rank, student in enumerate(students, start=1):
        print("\nRank:", rank)
        print("Name:", student["name"])
        print("Aggregate:", student["aggregate"], "%")
        print("Attendance:", student["attendance"], "%")
        print("Family Income: Rs.", student["income"])
else:
    print("No eligible students found.")

print("\nProgram Completed.")
