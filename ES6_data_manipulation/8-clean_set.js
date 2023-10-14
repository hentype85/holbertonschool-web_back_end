export default function cleanSet(set, startString) {
  if (startString === "" || typeof startString !== "string") {
    return "";
  }

  let result = "";

  set.forEach((value) => {
    if (value.startsWith(startString)) {
      const trimmedValue = value.substring(startString.length);
      if (result !== "") {
        result += "-";
      }
      result += trimmedValue;
    }
  });

  return result;
}
