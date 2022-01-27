class MyCounterV2:
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        self.value = self.value + self.step

    def count_down(self):
        self.value = self.value - self.step

