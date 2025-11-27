def sol_detox(a, b, c):
    # проверка корректности входа
    assert(1 <= a <= 100000)
    assert(1 <= b <= 100000)
    assert(1 <= c <= 100000)

    ans = []
    x = 0
    while a * x <= c:
        if (c - a * x) % b == 0:
            y = (c - a * x) // b
            ans.append((x, y))
        x += 1

    return ans


if __name__ == "__main__":
    # здесь задаются тестовые входные данные
    a = 50
    b = 30
    c = 900
    ans = sol_detox(a, b, c)
    print(f"answer = {ans}")
