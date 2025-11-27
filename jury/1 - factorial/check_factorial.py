# Здесь задается абсолютный путь к решению участника,
#   модуль импортируется, и решение запускается

if __name__ == "__main__":
    import sys
    sys.path.append('..')
    from config import root_contestant
    sys.path.append('../' + root_contestant + '/1 - factorial')

from sol_factorial import sol_factorial as sol_contestant
#from sol_jury_factorial import sol_factorial as sol_contestant
from sol_jury_factorial import sol_factorial as sol_jury


class Solution:
    def __init__(self, run_callback):
        self.run_callback = run_callback

def check_output(input, output, answer):
    if answer == (-1, -1):
        return output == (-1, -1)
    else:
        n = output[0]
        k = output[1]
        n_ans = answer[0]
        k_ans = answer[1]
        assert(n_ans >= 1 and n_ans <= 10)
        if k == k_ans:
            n = output[0]
            k = output[1]
            n_ans = answer[0]
            k_ans = answer[1]
            return n_ans == n and k_ans == k
            # на тестовых примерах ответ единственный
            # на тестах жюри будет использована более точная проверка
        else:
            return False

class UnitTest:
    pass

class UnitTest_GivenAnswer(UnitTest):
    def __init__(self, input, answer):
        self.input = input
        self.answer = answer
    def run(self, sol):
        output = sol.run_callback(self.input)
        return check_output(self.input, output, self.answer)

class UnitTest_JuryAnswer(UnitTest):
    def __init__(self, input, sol_etalon):
        self.input = input
        self.sol_etalon = sol_etalon
    def run(self, sol):
        output = sol.run_callback(self.input)
        answer = self.sol_etalon.run_callback(self.input)
        return check_output(self.input, output, answer)


# Тест 1
M = 4320
n, k = (8, 1)
test_1 = UnitTest_GivenAnswer(M, (n, k))

# Тест 2
M = 38
n, k = (9, 4)
test_2 = UnitTest_GivenAnswer(M, (n, k))

# Тест 3
M = 399168
n, k = (-1, -1)
test_3 = UnitTest_GivenAnswer(M, (n, k))

# Тест 4
M = 83
n, k = (-1, -1)
test_4 = UnitTest_GivenAnswer(M, (n, k))

sol_etalon = Solution(sol_jury)

# Тесты 5-70
M_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            22, 23, 24, 25, 32, 37, 40, 41, 42, 43, 44, 45, 50, 52, 74, 82, 94, 99, 100,
            1123, 3214, 5791, 48901, 577001, 628800, 362880, 362800, 36288, 362880, 6288, 362, 628,
            400, 320, 720, 270, 72, 27, 504, 5040, 2005040, 504099, 7777, 99990, 999999, 3000000]
tests_5_70 = [UnitTest_JuryAnswer(M, sol_etalon) for M in M_values]


test_case = [test_1, test_2, test_3, test_4] + tests_5_70
sol = Solution(sol_contestant)
overall_result = True
print("1 - factorial")
for test_num, test in enumerate(test_case):
    result = test.run(sol)
    text_result = "Pass" if result else "Fail"
    print(f"Test {test_num + 1} - {text_result}")
    overall_result = overall_result and result
text_overall_result = "Accepted" if overall_result else "Rejected"
print(f"-------\nResult: {text_overall_result}\n")