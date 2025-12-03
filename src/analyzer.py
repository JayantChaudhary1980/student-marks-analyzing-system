from collections import defaultdict
from typing import Dict, List, Tuple

from .models import Student, MarkRecord, StudentResult


class MarksAnalyzer:
    """
    Contains all business logic for analyzing student marks.
    """

    def __init__(self, students: Dict[str, Student], records: List[MarkRecord]):
        self.students = students
        self.records = records

    def build_student_results(self) -> Dict[str, StudentResult]:
        subject_marks_map: Dict[str, Dict[str, float]] = defaultdict(dict)

        for record in self.records:
            subject_marks_map[record.student_id][record.subject] = record.marks

        results: Dict[str, StudentResult] = {}
        for sid, subjects in subject_marks_map.items():
            total = sum(subjects.values())
            average = total / len(subjects) if subjects else 0.0
            grade = self._calculate_grade(average)
            results[sid] = StudentResult(
                student=self.students[sid],
                subject_marks=subjects,
                total=total,
                average=average,
                grade=grade
            )
        return results

    @staticmethod
    def _calculate_grade(average: float) -> str:
        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def class_average(self) -> float:
        if not self.records:
            return 0.0
        total = sum(r.marks for r in self.records)
        return total / len(self.records)

    def subject_toppers(self) -> Dict[str, Tuple[Student, float]]:
        subject_best: Dict[str, Tuple[str, float]] = {}
        for r in self.records:
            if r.subject not in subject_best or r.marks > subject_best[r.subject][1]:
                subject_best[r.subject] = (r.student_id, r.marks)

        result: Dict[str, Tuple[Student, float]] = {}
        for subject, (sid, marks) in subject_best.items():
            result[subject] = (self.students[sid], marks)
        return result
