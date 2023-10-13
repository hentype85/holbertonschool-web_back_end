export default function getStudentsByLocation(students, city) {
  // check students is an array
  if (Object.getPrototypeOf(students) === Array.prototype) {
    return students.filter((student) => student.location === city);
  }
  return [];
}
