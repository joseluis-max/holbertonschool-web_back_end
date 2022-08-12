export default function updateUniqueItems(map) {
  if (map instanceof Map) {
    map.forEach((value, key) => {
      if (value === 1) {
        map.set(key, 100);
      }
    });
  } else {
    throw new Error('Cannot process');
  }
  return map;
}
