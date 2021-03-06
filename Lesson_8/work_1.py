# Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.


s = 'papapapa'


def search_strings(s):
    n = len(s)
    arr_str = set()
    for i in range(1, n):

        for j in range(n - i + 1):

            k = hash(s[j:j+i])

            if k not in arr_str:
                arr_str.add(k)

    return len(arr_str)


print(f'Количество подстрок: {search_strings(s)}')