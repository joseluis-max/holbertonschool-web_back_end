export default function getStudentIdsSum(listStudents) {
  return listStudents.reduce((previous, studentB) => previous + studentB.id, 0);
}
