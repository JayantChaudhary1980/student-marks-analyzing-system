from dataclasses import dataclass
from typing import Dict


@dataclass
class Student:
    student_id: str
    name: str
    class_name: str  


@dataclass
class MarkRecord:
    student_id: str
    subject: str
    marks: float  


@dataclass
class StudentResult:
    student: Student
    subject_marks: Dict[str, float]
    total: float
    average: float
    grade: str
