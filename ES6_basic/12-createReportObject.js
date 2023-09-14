export default function createReportObject(employeesList) {
  const allEmployees = {
    ...employeesList,
  };

  function getNumberOfDepartments() {
    const keys = Object.keys(allEmployees);
    return keys.length;
  }

  return { allEmployees, getNumberOfDepartments };
}
