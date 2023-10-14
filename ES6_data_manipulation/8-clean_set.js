export default function cleanSet(set, startString) {
  const arr = [];

  if (typeof startString !== 'string' || startString === '') {
    return '';
  }

  for (const v of set) {
    if (v !== undefined && typeof startString === 'string' && v.startsWith(startString)) {
      arr.push(v.substring(startString.length));
    }
  }

  return arr.join('-');
}
