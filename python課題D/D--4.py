class MyCounterV1:

    def __init__(self, value):
        self.value = value

    def count_up(self):
        self.value += 1


counter1 = MyCounterV1(value=0)
print(counter1.value)  # 0

counter1.count_up()
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 2
