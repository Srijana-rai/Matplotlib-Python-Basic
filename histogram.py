import matplotlib.pyplot as plt

marks = [45,78,55,88,35,70,92,48,80,60]

plt.yticks(range(0,5))
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.title("Distribution of Exam Scores")

plt.hist(marks,bins=5, edgecolor="black")
plt.show()