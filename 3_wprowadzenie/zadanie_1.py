#Zdefiniuj następujące zbiory, wykorzystując Python comprehension
#A={1/x: x(<1,10>}
#B={1,2,4,8,..,2^10}
#C={x:x(B i x jest liczbą podzielną przez 4}

import sys

sys.stdout.write("A = ")
A=[round(1/x, 2) for x in range(1, 11)]
print(A)

sys.stdout.write("B = ")
B=[2**x for x in range(11)]
print(B)

sys.stdout.write("C = ")
C=[x for x in B if x%4==0]
print(C)