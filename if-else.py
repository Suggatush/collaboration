#Isaac Williams
#honorroll.py
# This program allows for name and gpa input and test whether student has met criteria for honor roll or deans list
import sys
last_name = input(str("What is the student's last name?"))
if last_name == "ZZZ":
  sys.exit()
first_name = input(str("What is the student's first name?"))
gpa_str = input(str("What is the student's gpa?"))
gpa = float(gpa_str)
if gpa >= 3.5:
  print("The student has made the Dean's list!")
elif gpa >= 3.25:
  print("The student has made the Honor Roll")
else:
  print("The student has not made the requirements for the Honor Roll or Dean's list")