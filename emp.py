class Employee:
    def __init__(self,first,last,email,pay):
        self.first=first
        self.last=last
        self.email=email
        self.pay=pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1= Employee("Pramod","Jana","Pramodjana395@gmail.com",50000)
emp_2= Employee("Shivani","Konar","mamonikonar512@gmail.com",60000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())
