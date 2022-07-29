export default function createReportObject(employeesList) {
  return {
    allEmployees: employeesList,
    getNumberOfDepartments: (dict) => Object.keys(dict).length,
  };
}
