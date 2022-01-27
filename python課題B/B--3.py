wide = int(input('行数を入力してください'))
height = int(input('列数を入力してください'))
n = 1
k = 1
while n <= height:
    while k <= wide:
        print(str(k) + '    x  ' + str(n) + '   =   ' + str(n * k) + '  |', end='\t')
        k += 1

    print('')
    k = 1
    n += 1
