# Zaimportuj pakiet itertools i znajdź w jego dokumentacji sposób na wygenerowanie kombinacji
# 3 elementowych bez powtórzeń na zbiorze 10 elementowym.

import itertools

result_0 = itertools.combinations('0123456789', 3)
result_1 = itertools.combinations('ABCDEFGHIJ', 3)

for x in range(0, 120):
    print(next(result_0), end="   ")
    print(next(result_1))