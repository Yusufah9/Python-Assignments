grade1 = "A"
grade2 = "B"
grade3 = "C"
grade4 = "D"  # Changed from "Average" to match prompt requirements
grade5 = "E"

score = int(input("Enter your score between 0 - 100: "))

if 90 <= score <= 100:
    print(grade1)
elif 80 <= score < 90:   # Changed <= to < to avoid overlapping grades
    print(grade2)
elif 70 <= score < 80:
    print(grade3)
elif 60 <= score < 70:
    print(grade4)
elif 55 <= score < 60:
    print(grade5)
else:
    print("Failing Grade")

