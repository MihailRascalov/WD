# Przepisz jeden z napisanych przez siebie iteratorów na generator.

def vowel_generator(data):
    """Generator that returns even values"""
    if isinstance(data, str):
        vowel_list = ['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y']
        for index in range (0, len(data)):
            if data[index] in vowel_list:
                yield data[index]
    else:
        print("Wrong argument type")

try:
    generator_test_string = vowel_generator("Brzęczyszczykiewicz")
    for x in range(0, 6):
        print(next(generator_test_string))
    print()

    generator_test_int = vowel_generator(512321)
    print(next(generator_test_int))
except StopIteration:
    print("StopIteration exception")
except Exception:
    print("General exception")