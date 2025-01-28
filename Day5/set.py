empty_set = set() or {}
fruits = {'apple', 'banana', 'cherry'}
print("Empty set:", empty_set)
print("Fruits set:", fruits)

fruits.add('orange')
print("Fruits set after adding orange:", fruits)

fruits.remove('banana')
print("Fruits set after removing banana:", fruits)

fruits.clear()
print("Fruits set after clearing:", fruits)

fruits.update(['apple', 'banana', 'cherry'])
print("Fruits set after updating:", fruits)

