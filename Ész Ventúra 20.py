"""
Ész Ventuúra 20.

Létezik-e olyan tört, aminek a nevezője és a számlálója is négyjegyű,
a nevező és számláló számjegyei mind különbözőek,
tehát a törtben nincs két azonos számjegy,
továbbá egyik számjegy sem nulla, és a tört értéke
egy egyjegyű pozitív egész szám,
mégpedig pont az a szám, azaz számjegy, ami kimaradt,
azaz nem szerepel a tört számjegyei között?
"""
import itertools
import pprint
permutations = list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9]))
pp = pprint.PrettyPrinter()
# pp.pprint(permutations)
for element in permutations:
    i = ((1000 * element[0] +
         100 * element[1] +
         10 * element[2] +
         element[3]) /
         (1000 * element[4] +
         100 * element[5] +
         10 * element[6] +
         element[7]))
    if i == element[8]:
        pp.pprint(element)
        print("{0}{1}{2}{3}/{4}{5}{6}{7}={8}".format(element[0],
                                                     element[1],
                                                     element[2],
                                                     element[3],
                                                     element[4],
                                                     element[5],
                                                     element[6],
                                                     element[7],
                                                     element[8]))
