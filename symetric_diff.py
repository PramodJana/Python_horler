# Enter your code here. Read input from STDIN. Print output to STDOUT
n1=(input())
myset1= set()
for i in range(eval(n1)):
    myset1.add(input())



n2=input()
myset2= set()
for i in range(eval(n2)):
    myset2.add(input())

myset3=myset1.intersection(myset2)
myset4=myset1.union(myset2)

myset5=myset4.difference(myset3)



for i in (sorted(myset5,reverse=True)):
	print(i)