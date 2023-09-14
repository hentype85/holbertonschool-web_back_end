export default function appendToEachArrayValue(array, appendString) {
    const array_new = [];

    for (let i = 0; i < array.length; i++) {
      let value = array[i];
      array_new.push(appendString + value);
    }
  
    return array_new;
  }
