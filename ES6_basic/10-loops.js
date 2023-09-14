export default function appendToEachArrayValue(array, appendString) {
    for (let value of array) {
      array.push(appendString + value);
    }

    return array;
}
