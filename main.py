#Author: Jason Turney jnt5211@psu.print

grade1 = str(input("Enter your course 1 letter grade: "))
credit1 = float(input("Enter your course 1 credit: "))

if grade1 == "A":
  gradepoint1 = 4.0
elif grade1 == "A-":
  gradepoint1 = 3.67
elif grade1 == "B+":
  gradepoint1 = 3.33
elif grade1 == "B":
  gradepoint1 = 3.0
elif grade1 == "B-":
  gradepoint1 = 2.67
elif grade1 == "C+":
  gradepoint1 = 2.33
elif grade1 == "C":
  gradepoint1 = 2.0
elif grade1 == "D":
  gradepoint1 = 1.0
else:
  gradepoint1 = 0

grade2 = str(input("Enter your course 2 letter grade: "))
credit2 = float(input("Enter your course 2 credit: "))

if grade2 == "A":
  gradepoint2 = 4.0
elif grade2 == "A-":
  gradepoint2 = 3.67
elif grade2 == "B+":
  gradepoint2 = 3.33
elif grade2 == "B":
  gradepoint2 = 3.0
elif grade2 == "B-":
  gradepoint2 = 2.67
elif grade2 == "C+":
  gradepoint2 = 2.33
elif grade2 == "C":
  gradepoint2 = 2.0
elif grade2 == "D":
  gradepoint2 = 1.0
else:
  gradepoint2 = 0

grade3 = str(input("Enter your course 3 letter grade: "))
credit3 = float(input("Enter your course 3 credit: "))

if grade3 == "A":
  gradepoint3 = 4.0
elif grade3 == "A-":
  gradepoint3 = 3.67
elif grade3 == "B+":
  gradepoint3 = 3.33
elif grade3 == "B":
  gradepoint3 = 3.0
elif grade3 == "B-":
  gradepoint3 = 2.67
elif grade3 == "C+":
  gradepoint3 = 2.33
elif grade3 == "C":
  gradepoint3 = 2.0
elif grade3 == "D":
  gradepoint3 = 1.0
else:
  gradepoint3 = 0

GPA = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3) 
print(f"Your GPA is: {GPA}")