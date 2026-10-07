# Beginner Guide: Packages, Imports, Libraries and Datasets

If you are new to Python/Java, do not worry about imports. They are simply tools that a program asks to use.

## 1. What is a library?
A library is a collection of ready-made code written by other programmers.

Examples:
- Matplotlib helps us draw graphs.
- NumPy helps us work with numerical arrays.
- pandas helps us work with table-like data.
- SciPy provides scientific/statistical functions.
- scikit-learn provides machine-learning algorithms.

## 2. What does import mean?
In Python, an import tells Python that we want to use code from another library or module. Python documentation describes modules as files containing Python definitions and statements, and the import statement makes another module available to the current program.

Example: import math
This means: load Python's math module so functions such as sqrt() can be used.

## 3. What does 'as' mean?
Example: import matplotlib.pyplot as plt
- matplotlib = the library/package
- pyplot = the graph-drawing part used here
- plt = short name we give it

Then plt.plot(x, y) uses Matplotlib's plotting functions.

## 4. Packages used in this repository
| Package / Module | Why we use it |
|---|---|
| math | Square root and mathematical calculations |
| numpy | Numerical arrays and numerical operations |
| pandas | Displaying and handling table-like data |
| scipy.stats | Statistical calculations such as Chi-Square |
| sklearn.cluster | K-Means clustering |
| sklearn.datasets | Creating sample datasets such as blobs |
| matplotlib.pyplot | Drawing graphs and charts |

Not every program needs a library. Most beginner programs use only variables, lists, loops, if/else, functions and print(). When no library is required, the code will explicitly say so in a comment.

## 5. Java packages
Many Java programs in this repository need no external package. They use basic Java features such as arrays, loops, if/else, String and Math. If there is no import line, that is intentional.

## 6. What is a dataset?
A dataset is the collection of data given to a data-mining program.

Example:
Height   Weight   Class
150      45       A
155      50       A
175      70       B

Each row is one record/object. Each column is an attribute. Class is the result/category when the experiment uses classification.

## 7. How our lab datasets work
### Classification
The dataset contains input attributes and a class. The program learns from existing records and predicts the class of a new record.

### K-Means
The dataset mainly contains numerical points. K-Means groups nearby points into clusters.

### Apriori / Association Rules
The dataset contains transactions. The program counts how often items occur together and finds frequent itemsets/rules.

### Chi-Square
The dataset is a frequency/contingency table. The program compares observed frequencies with expected frequencies.

### Dissimilarity Matrix
The dataset contains objects with numerical attributes. The program calculates the distance between every pair of objects and stores the results in a matrix.

### Visualization
The dataset contains values that can be represented using line graph, scatter plot, histogram, bar chart, box plot and pie chart.

## 8. The most important idea
DATASET -> PROGRAM / ALGORITHM -> CALCULATION -> OUTPUT -> OBSERVATION

The library is simply an additional toolbox used when the program needs a special operation such as plotting a graph or running a machine-learning algorithm.

## 9. Viva answers
Why did you import Matplotlib? — Matplotlib is a Python library used to create graphs and charts. I import pyplot so that I can plot the required visualizations.

Why did you import NumPy? — NumPy is used for numerical array operations and numerical data handling.

Why did you import pandas? — pandas is used to create and display table-like data in a convenient form.

Why did you import SciPy? — SciPy provides scientific and statistical functions. In the Chi-Square program I use its statistical function for the test.

Why did you import scikit-learn? — scikit-learn provides machine-learning algorithms. In our K-Means program it provides the KMeans algorithm.

What is your dataset? — The dataset is the collection of input records used by the algorithm. Each row represents an object or record and each column represents an attribute.

## Final rule for this repository
Every program should make these things clear:
1. What data are we using?
2. Why are we using this library/package?
3. What does each important import mean?
4. What happens to the dataset?
5. What algorithm is applied?
6. What output should we expect?
7. What observation can we write?

This guide is intentionally written for a beginner who is learning DWDM lab programming for the first time.