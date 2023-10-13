export default function updateStudentGradeByCity(students, city, newGrades) {
  // check students and newGrades are an array
  if (Object.getPrototypeOf(students) !== Array.prototype) {
    return [];
  }
  if (Object.getPrototypeOf(newGrades) !== Array.prototype) {
    return [];
  }

  return students.filter((student) => student.location === city).map((student) => {
    const [newGrade] = newGrades.filter((grade) => grade.studentId === student.id);
    return { ...student, grade: newGrade ? newGrade.grade : 'N/A' };
  });
}
