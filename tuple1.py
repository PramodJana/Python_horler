"""creating a tuple"""
tuple1=(40,50,40,"pramod")
print(tuple1)
print(type(tuple1))

tup=(10)
print(tup)
print(type(tup))

print(tuple1[3])
print(tuple1*3)

"""count and index function"""
print(tuple1.count(40))
print(tuple1.index("pramod"))

"""converting list to a tuple"""
list=[69,54,11]
print(type(list))
print(list)

lit=tuple(list)
print(type(lit))
print(lit)
