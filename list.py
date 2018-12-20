
"""created a list"""
lst=[10,20,"pramod",-10,30.5]
print(lst)
print(lst[3])
print(lst[3:5])
print(lst*4)


"""append function"""
lst.append(69)
print(lst)

"""remove function"""
lst.remove("pramod")
print(lst)


"""clear function
lst.clear()
print(lst)
"""
"""max function"""
print(max(lst))

"""min function"""
print(min(lst))

"""insert function"""
lst.insert(3,99)
print(lst)

"""sorting function"""
print(lst.sort())
"""asending order"""
lst.sort()
print(lst)

"""desending order"""
lst.sort(reverse=True)
print(lst)
