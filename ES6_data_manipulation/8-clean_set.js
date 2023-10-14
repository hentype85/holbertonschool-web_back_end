export default function cleanSet(set, startString) {
  if (startString && typeof startString === 'string') {
    const arrString = [];

    for (const item of set) {
      if (item.startsWith(startString)) {
        arrString.push(item.slice(startString.length));
      }
    }
    return arrString.join('-');
  }

  return '';
}
