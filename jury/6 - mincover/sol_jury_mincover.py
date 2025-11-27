# Решение заимствовано у участника
def sol_mincover(N, M, pages, subjects):
    # Преобразуем предметы в битовые маски
    subject_masks = [0] * N
    for i, subject_set in enumerate(subjects):
        for subject in subject_set:
            subject_masks[i] |= (1 << (subject - 1))

    target_mask = (1 << M) - 1

    # Используем словарь для экономии памяти
    dp = {0: (0, set())}

    for book_idx in range(N):
        book_mask = subject_masks[book_idx]
        book_pages = pages[book_idx]

        # Создаем копию для безопасного обновления
        new_dp = dp.copy()

        for mask, (current_sum, current_books) in dp.items():
            new_mask = mask | book_mask
            new_sum = current_sum + book_pages
            new_books = current_books | {book_idx + 1}

            # Обновляем если нашли лучшее решение
            if new_mask not in new_dp or new_sum < new_dp[new_mask][0]:
                new_dp[new_mask] = (new_sum, new_books)

        dp = new_dp

    return (dp[target_mask][0], dp[target_mask][1])

if __name__ == "__main__":
    # здесь задаются тестовые входные данные
    N = 5
    M = 5
    pages = [100, 50, 150, 75, 80]
    subjects = [{1, 3}, {1, 4}, {2}, {2, 5}, {3, 5}]
    min_sum, books_choice = sol_mincover(N, M, pages, subjects)
    print(f"sum = {min_sum}\nchoice = {books_choice}")
