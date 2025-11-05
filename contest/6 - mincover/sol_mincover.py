def sol_mincover(N, M, pages, subjects):
    # место для вашего кода
    min_sum = 0
    books_choice = {}
    return min_sum, books_choice


if __name__ == "__main__":
    # здесь задаются тестовые входные данные
    N = 5
    M = 5
    pages = [100, 50, 150, 75, 80]
    subjects = [{1, 3}, {1, 4}, {2}, {2, 5}, {3, 5}]
    min_sum, books_choice = sol_mincover(N, M, pages, subjects)
    print(f"sum = {min_sum}\nchoice = {books_choice}")
