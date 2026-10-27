
 

print("EXAMINATION RESULT AND GRACE-MARK VALIDATION")

student_name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

grace_limit = int(input("Enter maximum grace marks allowed: "))

total_marks = 0
total_maximum = 0
all_pass = True

for i in range(1, n + 1):

    print("\nSubject", i)

    subject = input("Enter subject name: ")
    maximum = int(input("Enter maximum marks: "))
    obtained = int(input("Enter obtained marks: "))
    passing = int(input("Enter passing marks: "))

    grace = 0

    
    if maximum <= 0 or passing < 0 or passing > maximum:
        print("Invalid subject marks or passing criteria")
        all_pass = False
        continue

    if obtained < 0 or obtained > maximum:
        print("Invalid obtained marks")
        all_pass = False
        continue

   
    if obtained >= passing:
        status = "PASS"

    else:
        required = passing - obtained

         
        if required <= grace_limit:
            grace = min(required, maximum - obtained)
            obtained += grace

            if obtained >= passing:
                status = "PASS"
            else:
                status = "FAIL"
                all_pass = False

        else:
            status = "FAIL"
            all_pass = False

    total_marks += obtained
    total_maximum += maximum

    print("Subject:", subject)
    print("Final Marks:", obtained)
    print("Grace Marks:", grace)
    print("Subject Result:", status)

 
if total_maximum > 0:
    percentage = (total_marks / total_maximum) * 100
else:
    percentage = 0

 
print("\n========== FINAL RESULT ==========")

print("Student Name:", student_name)
print("Total Marks:", total_marks, "/", total_maximum)
print("Percentage:", round(percentage, 2), "%")

if all_pass and total_maximum > 0:
    print("Final Classification: PASS")

    if percentage >= 75:
        print("Grade: DISTINCTION")
    elif percentage >= 60:
        print("Grade: FIRST CLASS")
    elif percentage >= 50:
        print("Grade: SECOND CLASS")
    else:
        print("Grade: PASS CLASS")

else:
    print("Final Classification: FAIL")

print("==================================")

