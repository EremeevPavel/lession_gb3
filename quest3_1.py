
def first_func(a, b):
    try:
        if not b == 0:
            res = a / b
            print(res)
    except:
        ZeroDivisionError()



a = int(input('Введи делимое!: '))
b = int(input('Введи делитель: '))
first_func(a, b)
