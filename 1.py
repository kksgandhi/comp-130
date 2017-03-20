from sets import Set
s = Set([1,2,3,4])
t=Set([3,4,5,6])
print(s.intersection(s.union(t)))
print(t.union(s))
