import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. LINE GRAPH
# ============================================================
x = np.arange(0, 10, 2)
y = x ** 2

print("X =", x)
print("Y =", y)

plt.figure()
plt.plot(x, y, marker="o")
plt.title("Line Graph")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# ============================================================
# 2. SCATTER PLOT
# ============================================================
x = [2, 4, 6, 8, 10, 12]
y = [50, 70, 20, 80, 90, 40]

plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# ============================================================
# 3. HISTOGRAM
# ============================================================
marks = [90, 95, 20, 35, 70, 75, 60, 65, 30, 55]
grade_intervals = [0, 50, 80, 100]

plt.figure()
plt.hist(marks, grade_intervals, histtype="bar", rwidth=0.7)
plt.title("Student Grade")
plt.xlabel("Percentage")
plt.ylabel("No. of Students")
plt.show()

# ============================================================
# 4. BAR CHART
# ============================================================
x = ["H", "E", "M", "A"]
y = [30, 50, 70, 90]

plt.figure()
plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()

# ============================================================
# 5. BOX PLOT
# ============================================================
list1 = [11, 4, 6, 8, 6, 9, 3]

plt.figure(figsize=(10, 7))
plt.boxplot(list1)
plt.title("Box Plot")
plt.show()

# ============================================================
# 6. PIE CHART
# ============================================================
student_performance = ["Excellent", "Good", "Average", "Poor"]
student_values = [35, 30, 20, 15]

plt.figure()
plt.pie(student_values, labels=student_performance)
plt.title("Pie Chart")
plt.show()

# Observation
print("Observation: Matplotlib can represent data using")
print("line graph, scatter plot, histogram, bar chart,")
print("box plot and pie chart.")
