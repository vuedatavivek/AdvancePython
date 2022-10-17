# max() - Returns the largest item in an iterable
# min() - Returns the smallest item in an iterable
# iter() - Returns an iter object
# Reverse() - Returns a reversed iterator
# next() - Returns the next item in an iterable
# slice() - Returns a slice object
# sorted() - Returns a sorted list
# sum() - Sums the items of an iterator
# input() - Allows user to input value
from re import X


demo_tuple = (1,3,6,4,9,12,43,15,67)
# x = max(demo_tuple)
# print(x)
# x = min(demo_tuple)
# print(x)
x = iter(demo_tuple)
y = reversed(demo_tuple)
print(next(x))
print(next(x))
print(next(y))
x= slice(1,5)
print(demo_tuple[x])
x = sorted(demo_tuple)
print(x)
x = sum(demo_tuple)
print(x)
print("Enter Input :")
x = input()
print(x)

