"""creating set"""
s={10,20,30,40}
print(s)
print(type(s))


"""set dosen't allow duplicate elements"""
s1={10,101,0,10,10}
print(s1)


"""update function"""
s.update([11,22])
print(s)

"""set dosent support indexing and slicing and it also not allow replication"""
s1.remove(10)
print(s1)
