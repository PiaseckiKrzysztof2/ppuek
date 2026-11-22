# Zadanie 7-3.20 - Program używający modułu MyArrays
# Co robi: dla liczb 7, 3, 8, 5, 2 wypisuje (funkcjami z modułu MyArrays): drugą największą (7),
#          różnicę max-min (6), medianę (5), najmniejszą i największą (2,8) i liczby jako 7-3-8-5-2.

import MyArrays

numbers = [7, 3, 8, 5, 2]

print('Numbers:', MyArrays.to_string(numbers, ','))
print('Second largest number:', MyArrays.second_largest(numbers))
print('Difference between largest and smallest:', MyArrays.difference(numbers))
print('Median:', MyArrays.median(numbers))
print('Smallest and largest number:', MyArrays.to_string(MyArrays.smallest_largest(numbers), ','))
print('Numbers as a string:', MyArrays.to_string(numbers))
