from dataclasses import dataclass
from typing import Dict


@dataclass
class Student:
    student_id: str
    name: str
    class_name: str  # e.g. "CSE-2A"


@dataclass
class MarkRecord:
    student_id: str
    subject: str
    marks: float  # 0 - 100


@dataclass
class StudentResult:
    student: Student
    subject_marks: Dict[str, float]
    total: float
    average: float
    grade: str
