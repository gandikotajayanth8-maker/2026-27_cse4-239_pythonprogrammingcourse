# 1. University Scholarship Allocation System

## 1. Problem Statement

The University Scholarship Allocation System is designed to identify and rank eligible students based on their academic performance, attendance, and family income.

The system evaluates students using the following criteria:

1. Aggregate Marks: Students must score a minimum of 75% aggregate marks.
2. Subject-wise Minimum Scores: Students must score at least 60 marks in every subject.
3. Attendance: Students must have at least 75% attendance.
4. Family Income: Annual family income must not exceed ₹2,50,000.

The system checks all eligibility conditions, selects qualified students, ranks them based on aggregate marks, and resolves ties using attendance and family income criteria.

## 2. Algorithm

Step 1: Start the program.

Step 2: Read the number of students.

Step 3: For each student, input:

- Student name
- Aggregate percentage
- Subject-wise marks
- Attendance percentage
- Annual family income

Step 4: Check eligibility conditions:

- Aggregate marks >= 75
- Every subject mark >= 60
- Attendance >= 75
- Family income

Flowchart Explanation:

1. Start the program.
2. Enter student details.
3. Check aggregate marks.
4. Check subject-wise minimum marks.
5. Check attendance.
6. Check family income.
7. If all conditions are satisfied, add the student to the eligible list.
8. Rank eligible students.
9. Display the scholarship ranking.
10. End the program.

## 4. Python Source Code

```
# University Scholarship Allocation Systemstudents = []n = int(input("Enter number of students: "))for i in range(n):    print("\nEnter details of Student", i + 1)    name = input("Enter student name: ")    aggregate = float(input("Enter aggregate marks (%): "))    subjects = int(input("Enter number of subjects: "))    marks = []    for j in range(subjects):        mark = float(input(f"Enter marks in subject {j + 1}: "))        marks.append(mark)    attendance = float(input("Enter attendance (%): "))    income = float(input("Enter annual family income: "))    # Eligibility checking    if (aggregate >= 75 and        all(mark >= 60 for mark in marks) and        attendance >= 75 and        income <= 250000):        students.append({            "name": name,            "aggregate": aggregate,            "attendance": attendance,            "income": income        })
```

## 5. Sample Input

```
Enter number of students: 4

Enter details of Student 1
Enter student name: Ravi
Enter aggregate marks (%): 85
Enter number of subjects: 3
Enter marks in subject 1: 80
Enter marks in subject 2: 85
Enter marks in subject 3: 90
Enter attendance (%): 90
Enter annual family income: 200000

Enter details of Student 2
Enter student name: Sita
Enter aggregate marks (%): 92
Enter number of subjects: 3
Enter marks in subject 1: 90
Enter marks in subject 2: 95
Enter marks in subject 3: 91
Enter attendance (%): 95
Enter annual family income: 180000

Enter details of Student 3
Enter student name: Kumar
Enter aggregate marks (%): 70
Enter number of subjects: 3
Enter marks in subject 1: 75
Enter marks in subject 2: 70
Enter marks in subject 3: 80
Enter attendance (%): 85
Enter annual family income: 150000

Enter details of Student 4
Enter student name: Priya
Enter aggregate marks (%): 85
Enter number of subjects: 3
Enter marks in subject 1: 80
Enter marks in subject 2: 85
Enter marks in subject 3: 90
Enter attendance (%): 95
Enter annual family income: 150000
```

## 6. Sample Output

```
Ravi is Eligible for Scholarship
Sita is Eligible for Scholarship
Kumar is Not Eligible for Scholarship
Priya is Eligible for Scholarship

===== SCHOLARSHIP RANK LIST =====

Rank: 1
Name: Sita
Aggregate: 92.0 %
Attendance: 95.0 %
Family Income: Rs. 180000.0

Rank: 2
Name: Priya
Aggregate: 85.0 %
Attendance: 95.0 %
Family Income: Rs. 150000.0

Rank: 3
Name: Ravi
Aggregate: 85.0 %
Attendance: 90.0 %
Family Income: Rs. 200000.0

Program Completed.
```

Result: The system successfully identifies eligible students and ranks them according to aggregate marks, attendance, and family income.

## 7. Mermaid Flowchart Code

<img width="1428" height="1978" alt="mermaid-diagram" src="https://github.com/user-attachments/assets/1ab726dd-947e-482a-86cb-cb867e250bfc" />
 

## Conclusion

The University Scholarship Allocation System helps universities select deserving students for scholarships by considering academic performance, subject-wise marks, attendance, and family income. It automatically checks eligibility, ranks qualified students, and resolves ties using predefined rules. This system makes scholarship allocation easier, faster, and more transparent.

Tip: For your practical record, include the problem statement, algorithm, flowchart, Python source code, sample input, sample output, and conclusion in this order.
