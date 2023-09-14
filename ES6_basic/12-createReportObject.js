export default function createReportObject(employeesList) {
  const allEmployees = {
    ...employeesList,
  };

  function getNumberOfDepartments() {
    let keys = Object.keys(allEmployees);
    return keys.length;
  }

  return { allEmployees, getNumberOfDepartments };
}
