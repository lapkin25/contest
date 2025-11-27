if __name__ == "__main__":
    import sys
    sys.path.append('..')
    from config import root_contestant
    sys.path.append('../' + root_contestant + '/6 - mincover')

from sol_mincover import sol_mincover as sol_contestant
#from sol_jury_mincover import sol_mincover as sol_contestant
from sol_jury_mincover import sol_mincover as sol_jury

import random

class Solution:
    def __init__(self, run_callback):
        self.run_callback = run_callback

def check_output(input, output, answer):
    N = input[0]
    M = input[1]
    pages = input[2]
    subjects = input[3]
    min_sum = output[0]
    books_choice = output[1]
    min_sum_ans = answer[0]
    books_choice_ans = answer[1]
    # проверяем, что найдена минимальная сумма страниц
    if min_sum != min_sum_ans:
        return False
    # проверяем сумму страниц
    sum_pages = sum([pages[book - 1] for book in books_choice])
    if sum_pages != min_sum:
        return False
    # проверяем, что выбранные книги покрывают все предметы
    subjects_covered = set()
    for book in books_choice:
        subjects_covered = subjects_covered.union(subjects[book - 1])
    if len(subjects_covered) != M:
        return False
    return True


class UnitTest:
    pass

class UnitTest_GivenAnswer(UnitTest):
    def __init__(self, input, answer):
        self.input = input
        self.answer = answer
    def run(self, sol):
        output = sol.run_callback(*self.input)
        return check_output(self.input, output, self.answer)

class UnitTest_JuryAnswer(UnitTest):
    def __init__(self, input, sol_etalon):
        self.input = input
        self.sol_etalon = sol_etalon
    def run(self, sol):
        output = sol.run_callback(*self.input)
        answer = self.sol_etalon.run_callback(*self.input)
        return check_output(self.input, output, answer)

class UnitTest_Generator_1(UnitTest_JuryAnswer):
    def __init__(self, seed, N, M, sol_etalon):
        random.seed(seed)
        # генерируем input
        pages = []
        subjects = []
        for i in range(N):
            pages.append(random.choice(range(1, 1001)))
            subj_set = set()
            for j in range(1, M + 1):
                if random.random() < 0.3:
                    subj_set.add(j)
            subjects.append(subj_set)
        self.input = (N, M, pages, subjects)
        self.sol_etalon = sol_etalon


# Тест 1
N = 5
M = 5
pages = [100, 50, 150, 75, 80]
subjects = [{1, 3}, {1, 4}, {2}, {2, 5}, {3, 5}]
ans = (205, {2, 4, 5})
test_1 = UnitTest_GivenAnswer((N, M, pages, subjects), ans)

# Тест 2
N = 4
M = 2
pages = [10, 20, 30, 40]
subjects = [set(), {1, 2}, {2}, {1}]
ans = (20, {2})
test_2 = UnitTest_GivenAnswer((N, M, pages, subjects), ans)


sol_etalon = Solution(sol_jury)

# Тест 3
test_3 = UnitTest_Generator_1(123, 30, 5, sol_etalon)

# Тест 4
test_4 = UnitTest_Generator_1(12345, 50, 8, sol_etalon)

# Тест 5
test_5 = UnitTest_Generator_1(1234, 1000, 10, sol_etalon)


test_case = [test_1, test_2, test_3, test_4, test_5]
sol = Solution(sol_contestant)
overall_result = True
print("6 - mincover")
for test_num, test in enumerate(test_case):
    result = test.run(sol)
    text_result = "Pass" if result else "Fail"
    print(f"Test {test_num + 1} - {text_result}")
    overall_result = overall_result and result
text_overall_result = "Accepted" if overall_result else "Rejected"
print(f"-------\nResult: {text_overall_result}\n")