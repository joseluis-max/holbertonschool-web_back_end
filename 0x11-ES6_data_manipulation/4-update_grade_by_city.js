import getStudentsByLocation from "./2-get_students_by_loc"

export default function updateStudentGradeByCity(listStudents, city,  newGrades) {
  const list = getStudentsByLocation(listStudents, city);
  return list.map(student => {
    const list = newGrades.filter(grade => grade.studentId === student.id);
    if (list.length > 0) {
      student.grade = list[0].grade;
    } else {
      student.grade = "N/A";
    }
    return student;
  })
}
