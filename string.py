s="      you are awesome"
print(s)

s1="""you are
the creater
of your destiny"""
print(s1)

print(s[0])
print(s*2)
print(len(s1))
print(len(s))


"""slicing operation"""

print(s[0:5])
print(s[0:])
print(s[:8])
print(s[-3:-1])
print(s[0:9:2])
print(s[::-1])

"""strip the spaces"""

print(s.strip())
"""removing left spaces"""
print(s.lstrip())
"""removing right spaces"""
print(s.rstrip())


"""find function"""
print(s.find("awe",0,len(s)))

print(s.find("awe",0,8))

"""count function"""
print(s.count("a"))

"""replace function"""
print(s.replace("awesome","super"))
