# create an empty set
s = set()

# add some elements
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(4) # duplicate ignored

s.remove(2)

print(s)

print(f"The set has {len(s)} elements.") # len() returns the number of elements in a set