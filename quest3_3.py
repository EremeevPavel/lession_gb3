def my_funk(arg1, arg2, arg3):
    return arg1 + arg2 + arg3 - min(arg1, arg2, arg3)


res = my_funk(int(input('Введи первый аргумент: ')), int(input('Введи второй аргумент: ')),
              int(input('Введи третий аргумент: ')))
print(res)