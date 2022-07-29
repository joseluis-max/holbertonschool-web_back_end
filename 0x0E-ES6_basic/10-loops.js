export default function appendToEachArrayValue(array, appendString) {
  for (const idx of array) {
    newArr.push(appendString + idx);
  }

  return array;
}
