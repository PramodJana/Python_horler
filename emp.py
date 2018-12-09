class Employee:
    raise_amount=1.04



    def __init__(self,first,last,email,pay):
        self.first=first
        self.last=last
        self.email=email
        self.pay=pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay=int(self.pay *self.raise_amount)

emp_1= Employee("Pramod","Jana","Pramodjana395@gmail.com",50000)
emp_2= Employee("Shivani","Konar","mamonikonar512@gmail.com",60000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
