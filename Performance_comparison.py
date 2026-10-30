import matplotlib.pyplot as plt

marks = [[45,50,60,30,49],[30,45,60,50,55],[50,45,55,35,60]]
subjects = ["Maths","Science","Social","Nepali","English"]

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Marks Scored by students in Different Subjects")
for student_marks in marks:
    plt.plot(subjects,student_marks,marker="o")
plt.legend(["Student 1","Student 2", "Student 3"])
plt.show()