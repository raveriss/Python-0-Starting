#!/usr/bin/env python3

def my_range(mini, maxi, step):
    current = mini
    while current < maxi:
        yield(current)
        current += step
    return

r = my_range(0, 10, 2)
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
for value in r:
    print(value)  # Should print 0, 2, 4, 6, 8

for value in r:
    print(value) 






