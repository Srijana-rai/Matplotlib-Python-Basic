import matplotlib.pyplot as plt

study_hours = [2,5,3,6,1,4,7,2,5,3]
marks = [45,78,55,88,35,70,92,48,80,60]

 
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.yticks(range(0, 101, 5))
plt.title ("Study Hours vs Exam Score")
plt.scatter(study_hours,marks)
plt.show()