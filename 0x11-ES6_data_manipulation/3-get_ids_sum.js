export default function getStudentIdsSum(listStudents) {
  return listStudents.reduce((studentA, studentB) => studentA.id + studentB.id, 0);
}
