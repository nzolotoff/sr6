try :
    n = int(input('Введите количество элементов массива\n'))
    delta = int(input('Введите значение "Delta"\n'))
except ValueError :
    print('Введите целое число')
else :
    arr = []
    flag = True
    for i in range(n) :
        try:
            element = (int(input('Введите элемент массива\n')))
        except ValueError:
            print('Введите целое число')
            flag = False
            break
        else :
            arr.append(element)
    min = 2**1111
    for i in arr :
        if min > i :
            min = i
    result = min + delta
    count = 0
    for i in arr :
       if result == i :
            count +=1
    if flag != False :
        print('Количество совпадений равно {}'.format(count))


