# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
# A={1/x: xe<1,10>}
# B={1,2,4,8,..,2^10}
# C={x:xeB i x jest liczbą podzielną przez 4}

A = [round(1/x, 2) for x in range(1, 11)]
print("A = " + str(A))

B = [2**x for x in range(11)]
print("B = " + str(B))

C = [x for x in B if x%4==0]
print("C = " + str(C))