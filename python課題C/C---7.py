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
        if self.age < 20:
            return 1000
        elif self.age < 60 & self.age >= 20:
            return 1500
        else:
            return 1200

    def info_csv(self):
        list1 = [(str(Customer.full_naming(self)))]
        list1.append(str(self.age))
        list1.append(str((Customer.entry_fee(self))))
        i = ' '.join(list1)
        return i


ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.info_csv())
