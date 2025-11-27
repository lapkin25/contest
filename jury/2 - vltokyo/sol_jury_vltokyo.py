def is_capital_latin(word):
    ans = True
    for letter in word:
        ans = ans and (ord('A') <= ord(letter) <= ord('Z'))
    return ans

def sol_vltokyo(s, t):
    # проверка корректности входа
    assert(1 <= len(s) and len(s) <= 100)
    assert(1 <= len(t) and len(t) <= 10000)
    assert(all([1 <= len(word) <= 100 for word in s]))
    assert(all([1 <= len(word) <= 100 for word in t]))
    assert(all(map(is_capital_latin, s)))
    assert(all(map(is_capital_latin, t)))

    # собираем все префиксы слов из большого списка
    t_prefixes = set()
    for word in t:
        for i in range(len(word)):
            t_prefixes.add(word[:i + 1])
    # собираем все суффиксы слов из большого списка
    t_suffixes = set()
    for word in t:
        for i in range(len(word)):
            t_suffixes.add(word[i:])

    ans = []
    for word in s:
        longest_intersection_t_prefix = 0  # наибольшее пересечение с префиксами
        longest_intersection_t_suffix = 0  # наибольшее пересечение с суффиксами

        # ищем префиксы среди суффиксов
        for i in range(len(word)):
            prefix = word[:i + 1]
            len_prefix = i + 1
            # если префикс есть среди суффиксов, обновляем длину пересечения
            if prefix in t_suffixes:
                longest_intersection_t_suffix = max(longest_intersection_t_suffix, len_prefix)

        # ищем суффиксы среди префиксов
        for i in range(len(word)):
            suffix = word[i:]
            len_suffix = len(word) - i
            # если суффикс есть среди префиксов, обновляем длину пересечения
            if suffix in t_prefixes:
                longest_intersection_t_prefix = max(longest_intersection_t_prefix, len_suffix)

        best_words = []
        if longest_intersection_t_prefix >= longest_intersection_t_suffix:
            suffix = word[len(word) - longest_intersection_t_prefix : ]
            # берем все слова из t с подходящими префиксами
            for w in t:
                if w[:longest_intersection_t_prefix] == suffix:
                    best_words.append(w)
        if longest_intersection_t_prefix <= longest_intersection_t_suffix:
            prefix = word[:longest_intersection_t_suffix]
            # берем все слова из t с подходящими суффиксами
            for w in t:
                if w[len(w) - longest_intersection_t_suffix : ] == prefix:
                    best_words.append(w)
        ans.append(best_words)

    return ans


if __name__ == "__main__":
    # здесь задаются тестовые входные данные
    s = ['VLADIVOSTOK', 'AVATAR']
    t = ['TOKYO', 'VLADISLAV', 'VLAD', 'STOKS']

    ans = sol_vltokyo(s, t)
    print(f"answer = {ans}")
