import random

count = input('何回ころがしますか？')
aspect = input('さいころの面の数は')
total = []
for n in range(int(count)):

    total.append(random.randint(1, int(aspect)))

print(total)
