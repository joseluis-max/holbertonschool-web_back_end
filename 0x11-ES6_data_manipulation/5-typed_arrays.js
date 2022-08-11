export default function createInt8TypedArray(length, position, value) {
  let arr = new Int8Array(length);
  try {
    arr[position] = value;
  } catch (error) {
    throw new Error('Position outside range');
  }
  return arr;
}
