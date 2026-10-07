# DWDM Lab Programs — Beginner + Classroom Style

This repository is the **source of truth** for the DWDM lab.

## Beginner help before running programs

Read **00_BEGINNER_PACKAGE_DATASET_GUIDE.md** before running the Python/Java programs if packages, libraries, imports or datasets are new to you. It explains what each library means, why it is used, what the dataset contains, how the algorithm uses the dataset, and simple viva answers.

The important library-using Python files also contain these explanations directly as comments at the top of the code.

## What is included

### Programming style

Where programming is practical, the repository provides **both Java and Python** versions.

The programs now follow the same classroom style as the supplied lab examples:

- imports at the top when a package is required
- clear numbered **STEP 1, STEP 2, STEP 3...** sections
- simple variables, arrays/lists, loops and if/else
- comments explaining the purpose of each important block
- direct input -> processing -> output flow
- simple output statements that are easy to copy into a lab record
- no unnecessary advanced programming structures

For experiments where the supplied material uses standard packages such as **NumPy, Matplotlib, pandas, SciPy or scikit-learn**, those packages are used in the Python version so the program matches the classroom/reference style.

### Non-coding and WEKA experiments

The repository gives extra care to the non-coding parts:

- Aim
- Theory
- Step-by-step procedure
- Commands / settings
- What to record
- Observation
- Result
- Viva points where useful

For WEKA experiments, the WEKA procedure remains the main procedure because that is what the lab list asks for. Java/Python files are supplementary learning aids where appropriate.

## Folder map

01–07 → WEKA / warehouse / OLAP / classification / clustering / association / ZeroR  
08–16 → programming experiments  
ADDITIONAL → similarity/dissimilarity and linear regression

## Recommended lab workflow

1. Open `00_PROGRAM_INDEX.md`.
2. Open the required experiment folder.
3. Read `RECORD.md`.
4. Open the Python and Java program.
5. Read the numbered steps once.
6. Run the language required by your faculty.
7. Copy the output and observation into your record.

## Reference-style updates

- **Experiment 10:** Python follows the supplied Chi-Square example with NumPy, pandas and SciPy, including the observed table, expected table, Chi-Square value and observation.
- **Experiments 13 and 14:** Python follows the supplied K-Means style with Matplotlib, NumPy, scikit-learn, `make_blobs`, numbered steps and centroid plotting.
- **Experiment 16:** Python includes the supplied classroom chart style for line graph, scatter plot, histogram, bar chart, box plot and pie chart.

## Important

The sample datasets are educational examples. If your faculty gives a specific dataset, use that dataset for the actual lab record.

## Download

Use GitHub **Code → Download ZIP** to get a snapshot of the current repository.
