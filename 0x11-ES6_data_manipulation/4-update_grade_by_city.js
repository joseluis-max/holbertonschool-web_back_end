import getStudentsByLocation from "./2-get_students_by_loc"

export default function updateStudentGradeByCity(listStudents, city,  newGrades) {
  const list = getStudentsByLocation(listStudents, city);
  return list.map(student => {
    const grade = newGrades.filter(grade => grade.StudentId === student.id);
    if (grade) {
      student.grade = grade;
    } else {
      student.grade = "N/A";
    }
  })
}
