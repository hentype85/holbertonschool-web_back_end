export default function appendToEachArrayValue(array, appendString) {
  const arrayNew = [];

  for (let value of array) {
    arrayNew.push(appendString + value);
  }

  return arrayNew;
}
