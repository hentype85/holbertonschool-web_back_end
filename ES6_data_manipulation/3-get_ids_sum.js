export default function getStudentIdsSum (students) {
  // check students is an array
  if (Object.getPrototypeOf(students) === Array.prototype) {
    const studentIds = students.map(student => student.id);
    const sum = studentIds.reduce((accumulator, currentId) => accumulator + currentId, 0);

    return sum;
  }
  return [];
}
