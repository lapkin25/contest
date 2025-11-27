def sol_classify(x_train, y_train, x_test, y_test):
    assert(len(x_train) == len(y_train))
    assert(len(x_test) == len(y_test))
    assert(all([len(x_train[i]) == len(x_train[0]) for i in range(len(x_train))]))
    assert(all([len(x_test[i]) == len(x_test[0]) for i in range(len(x_test))]))
    assert(len(x_train[0]) == len(x_test[0]))
    N_train = len(y_train)
    N_test = len(y_test)
    d = 2
    for i in range(N_train):
        assert(y_train[i] == 0 or y_train[i] == 1)
        for k in range(d):
            assert(0 <= x_train[i][k] <= 1000)
    for i in range(N_test):
        assert(y_test[i] == 0 or y_test[i] == 1)
        for k in range(d):
            assert(0 <= x_test[i][k] <= 1000)
    # вычисляем координаты обоих центроидов
    centroid_1 = [0] * d  # центроид класса "1"
    centroid_0 = [0] * d  # центроид класса "0"
    # проверяем, что оба класса непусты (этого в условии не было; забыли написать, что классы непусты)
    N_1 = sum(y_train)
    N_0 = N_train - N_1
    assert(N_1 > 0 and N_0 > 0)
    for k in range(d):
        for i in range(N_train):
            if y_train[i] == 1:
                centroid_1[k] += x_train[i][k]
            else:
                centroid_0[k] += x_train[i][k]
        centroid_1[k] /= N_1
        centroid_0[k] /= N_0
    # классифицируем все точки тестовой выборки
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for i in range(N_test):
        # классифицируем i-ю точку
        y_pred = None
        sqr_distance_1 = sum([(x_test[i][k] - centroid_1[k]) ** 2 for k in range(d)])
        sqr_distance_0 = sum([(x_test[i][k] - centroid_0[k]) ** 2 for k in range(d)])
        if sqr_distance_1 - 1e-8 <= sqr_distance_0:
            y_pred = 1
        else:
            y_pred = 0
        if y_test[i] == 1:
            if y_pred == 1:
                TP += 1
            else:  # y_pred == 0
                FN += 1
        else:  # y_test[i] == 0
            if y_pred == 0:
                TN += 1
            else:  # y_pred == 1
                FP += 1
    return [[TN, FP], [FN, TP]]


if __name__ == "__main__":
    # здесь задаются тестовые входные данные
    x_train = [(120, 60), (100, 60), (140, 100), (140, 80)]
    y_train = [0, 0, 1, 1]
    x_test = [(125, 75), (140, 60), (140, 75), (110, 75)]
    y_test = [1, 1, 0, 0]
    ans = sol_classify(x_train, y_train, x_test, y_test)
    print(f"answer = {ans}")
