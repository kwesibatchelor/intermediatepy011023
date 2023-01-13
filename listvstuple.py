import sys
mylist  = [0, 1, 2, "Kwesi", True]
mytuple = (0, 1, 2, "Kwesi", True)
print(sys.getsizeof(mylist), "bytes")
print(sys.getsizeof(mytuple), "bytes")