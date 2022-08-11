export default function getListStudentIds(list) {
  try {
    return list.map((l) => l.id);
  } catch (error) {
    return [];
  }
}
