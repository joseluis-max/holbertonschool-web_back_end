export default function iterateThroughObject(reportWithIterator) {
  let newStr = '';
  let control = true;

  for (const employee of reportWithIterator) {
    if (control) {
      newStr += employee;
      control = false;
    } else {
      newStr += ` | ${employee}`;
    }
  }

  return newStr;
}
