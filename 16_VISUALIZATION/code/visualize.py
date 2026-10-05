import matplotlib.pyplot as plt

scores = [45, 55, 60, 62, 70, 72, 75, 80, 85, 90]
departments = ["CSE", "ECE", "EEE"]
students = [50, 35, 20]

plt.figure()
plt.hist(scores, bins=5)
plt.title("Score Histogram")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.boxplot(scores)
plt.title("Score Box Plot")
plt.show()

plt.figure()
plt.bar(departments, students)
plt.title("Students by Department")
plt.xlabel("Department")
plt.ylabel("Students")
plt.show()

plt.figure()
plt.pie(students, labels=departments, autopct="%1.1f%%")
plt.title("Department Distribution")
plt.show()