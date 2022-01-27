class Customer:
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name

    def full_naming(self):
        print(self.first_name + ' ' + self.family_name)


ken = Customer(first_name='ken', family_name='tanaka')
ken.full_naming()
tom = Customer(first_name='tom', family_name='ford')
tom.full_naming()
