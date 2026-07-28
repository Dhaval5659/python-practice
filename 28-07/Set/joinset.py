set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set4 = set1 | set2
print(set4)

myset = set1.union(set2, set4)
print(myset)

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

set1.update(set2)
print(set1)

# only keep duplicate
set10 = {"apple", "banana", "cherry"}
set20 = {"google", "microsoft", "apple"}

set30 = set10.intersection(set20)
print(set30)

set30 = set10 & set20
print(set30)

set10.intersection_update(set20)
print(set10)

set30 = set10.intersection(set20)
print(set30)

# defrance

set30 = set10.difference(set20)
print(set30)

set30 = set10 - set20
print(set30)

set10.difference_update(set20)
print(set10)

# symmetric defrance (show not same)
set30 = set10.symmetric_difference(set20)

print(set30)

set30 = set10 ^ set20
print(set30)

# in origin set instead of new set 
set1.symmetric_difference_update(set2)
print(set1)