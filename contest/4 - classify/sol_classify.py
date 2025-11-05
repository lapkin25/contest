def sol_classify(x_train, y_train, x_test, y_test):
    # место для вашего кода
    return [[0, 0], [0, 0]]


if __name__ == "__main__":
    # здесь задаются тестовые входные данные
    x_train = [(120, 60), (100, 60), (140, 100), (140, 80)]
    y_train = [0, 0, 1, 1]
    x_test = [(125, 75), (140, 60), (140, 75), (110, 75)]
    y_test = [1, 1, 0, 0]
    ans = sol_classify(x_train, y_train, x_test, y_test)
    print(f"answer = {ans}")
