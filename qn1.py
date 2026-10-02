name=input("Enter the student's name: ")
marks=[]
for i in range(3):
    mark=int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)
total=sum(marks)
average=total/3
highest=max(marks)
lowest=min(marks)
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"
print(f"Student Name: {name}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Highest Mark: {highest}")
print(f"Lowest Mark: {lowest}")
print(f"Grade: {grade}")