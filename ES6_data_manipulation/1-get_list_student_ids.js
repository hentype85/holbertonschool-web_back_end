export default function getListStudentIds(students) {
  if (!Array.isArray(students)) {
    return [];
  } else {
    return students.map((items) => items.id);
  }
}
