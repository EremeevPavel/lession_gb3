def int_func(word):
    return word.capitalize()


output = []
for word in input('Введите строку, слова в которой разделены пробелами: ').split(' '):
    output.append(int_func(word))

print(f'Строка получается вот такая: {" ".join(output)}')