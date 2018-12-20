dict1={"name":"pramod",2:"bill",3:"bc"}
print(dict1)

"""getting keys of a dictionary"""
k=dict1.keys()
for i in k:
    print(i)
"""getting values of a key"""
for i in dict1:
    print (dict1[i])

del dict1[3]
print(dict1)
