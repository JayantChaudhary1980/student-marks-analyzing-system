import csv
from pathlib import Path
from typing import List, Dict

from .models import Student, MarkRecord


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "marks.csv"


class MarksRepository:
    """
    Repository layer to handle reading and writing mark records
    from a CSV file. This keeps file handling separate from logic.
    """

    def __init__(self, data_file: Path = DATA_FILE):
        self.data_file = data_file
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.data_file.exists():
            # create file with header
            with self.data_file.open("w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["student_id", "student_name", "class_name", "subject", "marks"])

    def add_mark_records(self, records: List[MarkRecord], students: Dict[str, Student]) -> None:
        with self.data_file.open("a", newline="") as f:
            writer = csv.writer(f)
            for record in records:
                student = students[record.student_id]
                writer.writerow([
                    student.student_id,
                    student.name,
                    student.class_name,
                    record.subject,
                    record.marks
                ])

    def load_all(self) -> (Dict[str, Student], List[MarkRecord]):
        students: Dict[str, Student] = {}
        records: List[MarkRecord] = []

        if not self.data_file.exists():
            return students, records

        with self.data_file.open("r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                sid = row["student_id"]
                if sid not in students:
                    students[sid] = Student(
                        student_id=sid,
                        name=row["student_name"],
                        class_name=row["class_name"],
                    )
                records.append(
                    MarkRecord(
                        student_id=sid,
                        subject=row["subject"],
                        marks=float(row["marks"])
                    )
                )

        return students, records
