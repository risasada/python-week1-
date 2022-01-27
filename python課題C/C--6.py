class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_naming(self):
        full = (self.first_name + ' ' + self.family_name)
        str_full = ''.join(full)
        return str_full

    def entry_fee(self):
        if self.age <= 3:
            return 0
        elif self.age > 4 & self.age < 20:
            return 1000
        elif self.age < 60 & self.age >= 20:
            return 1500
        elif self.age >= 60 & self.age < 75:
            return 1200
        else:
            return 750


ken = Customer(first_name='ken', family_name='tanaka', age=3)
print(ken.entry_fee())
tom = Customer(first_name='tom', family_name='ford', age=73)
print(tom.entry_fee())
