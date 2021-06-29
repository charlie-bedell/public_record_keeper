class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job


    def __str__(self):
        print(f'<{self.__class__.__name__} => {self.name}>')
        attrs = self.__dict__
        for key in attrs:
            print(f'<{key} => {attrs[key]}>')
        return


    def last_name(self):
        return self.name.split()[-1]


    def give_raise(self, percent):
        self.pay *= (1.0 + percent)


if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    bob.__str__()
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    
    print(bob.last_name())
    print(sue.pay)
    sue.give_raise(.10)
    print(sue.pay)
    
    
    