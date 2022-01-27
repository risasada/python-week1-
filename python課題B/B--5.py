def total(num):
    tot = 0
    for i in range(0, len(num)):
        tot = tot + int(num[i])
    return tot


def maximum(arr1):
    numbers1 = 0
    i = 1
    while i < len(arr1):
        if arr1[numbers1] < arr1[i]:
            numbers1 = i
        i += 1

    return arr1[numbers1]


def minimum(arr2):
    numbers = 0
    for count in range(1, len(arr2)):
        if arr2[numbers] > arr2[count]:
            numbers = count

    return arr2[numbers]


def average(num):
    ave = total(num) / len(num)
    return round(ave, 2)


number = input('入力').split(' ')
print('合計：' + str(total(number)))
print('最大値:' + str(maximum(number)))
print('最小値:' + str(minimum(number)))
print('平均:' + str(average(number)))
