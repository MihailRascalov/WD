# Napisz generator, który będzie zwracał kolejne wartości ciągu Fibonacciego.

def fibonacci_generator():
    """Fibonacci generator makes next word in sequence using previous two"""
    a,b = 1,1
    yield a
    yield b
    while True:
        a,b = b,a+b
        yield b
        
g = fibonacci_generator()
for x in range(0, 101):
    print(next(g))