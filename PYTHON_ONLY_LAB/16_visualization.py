# EXPERIMENT 16 - DATASET VISUALIZATION
# Library used:
# matplotlib.pyplot -> used to draw graphs.
#
# Dataset = marks of nine subjects.
# If matplotlib is not installed:
# pip install matplotlib

import matplotlib.pyplot as plt

marks = [45, 55, 60, 60, 70, 72, 80, 85, 90]
subjects = ["C", "Java", "Python", "CN", "OS", "DBMS", "AI", "ML", "DM"]

print("DATASET =", marks)

# BAR CHART
plt.figure()
plt.bar(subjects, marks)
plt.title("Marks - Bar Chart")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# PIE CHART
plt.figure()
plt.pie(marks, labels=subjects, autopct="%1.0f%%")
plt.title("Marks - Pie Chart")
plt.show()

# HISTOGRAM
plt.figure()
plt.hist(marks, bins=5)
plt.title("Marks - Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# BOX PLOT
plt.figure()
plt.boxplot(marks)
plt.title("Marks - Box Plot")
plt.ylabel("Marks")
plt.show()

print("\nRESULT: Four basic visualizations were displayed.")
