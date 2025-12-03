# Student Marks Analyzing System

A simple command-line **Student Marks Analyzing System** written in Python as a Software Engineering mini-project.

## Objective

The goal of this project is to maintain student marks and perform basic analysis, such as:
- Calculating total and average marks per student
- Assigning grades based on average
- Finding subject-wise toppers
- Computing overall class statistics

The project demonstrates:
- Basic software engineering design (separation of concerns)
- File-based persistence (CSV)
- Simple, menu-driven user interaction

## Features

- Add a new student with multiple subject-wise marks
- Store data in a CSV file (`data/marks.csv`)
- View all student results:
  - Subject-wise marks
  - Total marks
  - Average marks
  - Grade (A+, A, B, C, D, F)
- View subject-wise toppers
- View overall class statistics (average, number of students, etc.)

## Project Structure

```text
student-marks-analyzing-system/
├─ src/
│  ├─ models.py        # Data models (Student, MarkRecord, StudentResult)
│  ├─ repository.py    # CSV read/write operations
│  ├─ analyzer.py      # Business logic for analysis
│  ├─ main.py          # Menu-driven UI, entry point
├─ data/
│  └─ marks.csv        # Data file (created automatically if missing)
├─ tests/
│  └─ sample_test_notes.txt  # Placeholder for test notes / future tests
├─ README.md
├─ requirements.txt
├─ .gitignore