#complex_numbers_one.py

def get_real_value(x, y):
    value = complex(x, y)
    return value.real

def get_imag_value(x, y):
    value = complex(x, y)
    return value.imag

print("The real part of complex number is: " 
        + str(get_real_value(4, 6)))
print("The imaginary part of complex number is: " 
        + str(get_imag_value(8, 8)))