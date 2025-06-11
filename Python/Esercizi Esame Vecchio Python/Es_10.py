def ricerca_binaria(array, target):
  sinistra = 0
  destra = len(array) - 1
  while sinistra <= destra:
    centro = (sinistra + destra) // 2
    if array[centro] == target:
      return centro
    elif array[centro] < target:
      sinistra = centro + 1
    else:
      destra = centro - 1
  return -1