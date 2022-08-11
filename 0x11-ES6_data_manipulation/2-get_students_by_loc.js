export default function getStudentsByLocation(listStudents, city) {
  return listStudents.filter((students) => students.location === city);
}
