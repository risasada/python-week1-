class Customer:

    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_naming(self):
        print(self.first_name + ' ' + self.family_name)


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.age)  # 15 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
print(tom.age) # 57 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.age)