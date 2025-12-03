import sys
from typing import Dict, List

from .models import Student, MarkRecord
from .repository import MarksRepository
from .analyzer import MarksAnalyzer


def input_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value < 0 or value > 100:
                print("Marks must be between 0 and 100.")
                continue
            return value
        except ValueError:
            print("Invalid number, try again.")


def add_student_flow(repo: MarksRepository) -> None:
    students_existing, _ = repo.load_all()

    student_id = input("Enter student ID (unique): ").strip()
    if student_id in students_existing:
        print("Student with this ID already exists in data file.")
        return

    name = input("Enter student name: ").strip()
    class_name = input("Enter class/section (e.g., CSE-2A): ").strip()

    subjects_input = input("Enter subjects separated by commas (e.g., Math,Physics,OS): ").strip()
    subjects = [s.strip() for s in subjects_input.split(",") if s.strip()]

    if not subjects:
        print("No subjects entered. Aborting.")
        return

    student = Student(student_id=student_id, name=name, class_name=class_name)

    records: List[MarkRecord] = []
    for subject in subjects:
        marks = input_float(f"Enter marks for {subject}: ")
        records.append(MarkRecord(student_id=student_id, subject=subject, marks=marks))

    repo.add_mark_records(records, {student_id: student})
    print("Student and marks saved successfully.")


def show_all_results(repo: MarksRepository) -> None:
    students, records = repo.load_all()
    if not students:
        print("No data found.")
        return

    analyzer = MarksAnalyzer(students, records)
    results = analyzer.build_student_results()

    print("\n=== Student Results ===")
    for sid, res in results.items():
        subs = ", ".join(f"{sub}:{m}" for sub, m in res.subject_marks.items())
        print(f"[{sid}] {res.student.name} ({res.student.class_name})")
        print(f"   Subjects: {subs}")
        print(f"   Total: {res.total:.2f}, Average: {res.average:.2f}, Grade: {res.grade}")
    print()


def show_subject_toppers(repo: MarksRepository) -> None:
    students, records = repo.load_all()
    if not students:
        print("No data found.")
        return

    analyzer = MarksAnalyzer(students, records)
    toppers = analyzer.subject_toppers()

    print("\n=== Subject-wise Toppers ===")
    for subject, (student, marks) in toppers.items():
        print(f"{subject}: {student.name} ({student.student_id}) - {marks} marks")
    print()


def show_class_stats(repo: MarksRepository) -> None:
    students, records = repo.load_all()
    if not students:
        print("No data found.")
        return

    analyzer = MarksAnalyzer(students, records)
    class_avg = analyzer.class_average()
    print("\n=== Class Statistics ===")
    print(f"Number of students: {len({r.student_id for r in records})}")
    print(f"Number of records: {len(records)}")
    print(f"Overall class average (all subjects): {class_avg:.2f}")
    print()


def main_menu():
    repo = MarksRepository()

    while True:
        print("====================================")
        print(" Student Marks Analyzing System ")
        print("====================================")
        print("1. Add new student and marks")
        print("2. View all student results")
        print("3. View subject-wise toppers")
        print("4. View class statistics")
        print("0. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student_flow(repo)
        elif choice == "2":
            show_all_results(repo)
        elif choice == "3":
            show_subject_toppers(repo)
        elif choice == "4":
            show_class_stats(repo)
        elif choice == "0":
            print("Exiting.")
            sys.exit(0)
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main_menu()
