from sol_mincover import sol_mincover

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
subjects = [{}, {1, 2}, {2}, {1}]
ans = (20, {2})
test_2 = UnitTest_GivenAnswer((N, M, pages, subjects), ans)


test_case = [test_1, test_2]
sol = Solution(sol_mincover)
overall_result = True
for test_num, test in enumerate(test_case):
    result = test.run(sol)
    text_result = "Pass" if result else "Fail"
    print(f"Test {test_num + 1} - {text_result}")
    overall_result = overall_result and result
text_overall_result = "Accepted" if overall_result else "Rejected"
print(f"-------\nResult: {text_overall_result}")
