# Stwórz listę składającą się z wartości zmiennoprzecinkowych a następnie zapisz do innej
# zmiennej jej kopię przekonwertowaną na typ int64.

import numpy as np

list = np.arange(1.1, 1.9, 0.1)
print(list.dtype)
list_converted_copy = list.astype("int64")
print(list_converted_copy.dtype)