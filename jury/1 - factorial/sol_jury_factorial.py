# минимальное число вычеркиваний, с помощью которых
#   из числа N можно получить число M
def calc_f(N, M):
    N_str = str(N)
    M_str = str(M)
    # заводим два курсора
    p = 0  # указывает на символ строки N_str
    q = 0  # указывает на символ строки M_str
    k = 0  # число вычеркиваний
    # жадный алгоритм: двигаем указатели и вычеркиваем не совпадающие символы
    while p < len(N_str) and q < len(M_str):
        if N_str[p] == M_str[q]:
            p += 1
            q += 1
        else:
            p += 1
            k += 1
    # если M_str не удалось получить, вычеркивая цифры из N_str, то
    #   значение функции f не определено
    if q < len(M_str):
        return None
    # вычеркиваем оставшиеся символы из N_str
    while p < len(N_str):
        p += 1
        k += 1
    return k


def sol_factorial(M):
    assert(1 <= M and M <= 3000000)
    fact = 1
    min_k = None
    best_i = None
    for i in range(1, 11):
        fact *= i
        # fact == factorial(i)
        k = calc_f(fact, M)
        if k is not None and (min_k is None or k < min_k):
            min_k = k
            best_i = i
    if min_k is None:
        return -1, -1
    else:
        return best_i, min_k


if __name__ == "__main__":
    # здесь задаются тестовые входные данные
    M = 4320
    n, k = sol_factorial(M)
    print(f"n = {n}\nk = {k}")
