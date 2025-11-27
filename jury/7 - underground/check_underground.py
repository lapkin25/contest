if __name__ == "__main__":
    import sys
    sys.path.append('..')
    from config import root_contestant
    sys.path.append('../' + root_contestant + '/7 - underground')

from sol_underground import sol_underground as sol_contestant
#from sol_jury_underground import sol_underground as sol_contestant
from sol_jury_underground import sol_underground as sol_jury

import random

class Solution:
    def __init__(self, run_callback):
        self.run_callback = run_callback

def check_output(input, output, answer):
    return len(output) == len(answer) and set(output) == set(answer)


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


# Тест 1
N = 3
pairs = [(1, 2), (2, 3)]
ans = [1, 2, 3]
test_1 = UnitTest_GivenAnswer((N, pairs), ans)

# Тест 2
N = 3
pairs = [(1, 3), (2, 3)]
ans = [3]
test_2 = UnitTest_GivenAnswer((N, pairs), ans)

# Тест 3
N = 4
pairs = [(1, 2), (3, 4)]
ans = []
test_3 = UnitTest_GivenAnswer((N, pairs), ans)


sol_etalon = Solution(sol_jury)

# Тест 4
N = 5
pairs = [(1, 2), (3, 4), (4, 5)]
test_4 = UnitTest_JuryAnswer((N, pairs), sol_etalon)

# Тест 5
N = 5
pairs = [(1, 2), (3, 4), (1, 4), (2, 3), (4, 5)]
test_5 = UnitTest_JuryAnswer((N, pairs), sol_etalon)

# Тест 6
N = 6
pairs = [(1, 2), (3, 4), (1, 4), (2, 3), (4, 5)]
test_6 = UnitTest_JuryAnswer((N, pairs), sol_etalon)

# Тест 7
N = 6
pairs = [(1, 2), (3, 4), (1, 4), (2, 3), (4, 5), (6, 3)]
test_7 = UnitTest_JuryAnswer((N, pairs), sol_etalon)

# Тест 8
N = 10
pairs = [(1, 5), (5, 8), (8, 10), (1, 9), (5, 9), (10, 9), (9, 6), (6, 7), (7, 3), (3, 4), (8, 9), (10, 2)]
test_8 = UnitTest_JuryAnswer((N, pairs), sol_etalon)

# Тест 9
N = 10
pairs = [(10, 9), (9, 8), (9, 7), (9, 6), (6, 5), (5, 4), (5, 3), (3, 2), (2, 1)]
test_9 = UnitTest_JuryAnswer((N, pairs), sol_etalon)

# Тест 10
N = 10
pairs = [(10, 9), (9, 8), (8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (4, 1)]
test_10 = UnitTest_JuryAnswer((N, pairs), sol_etalon)

test_case = [test_1, test_2, test_3, test_4, test_5, test_6, test_7, test_8, test_9, test_10]
sol = Solution(sol_contestant)
overall_result = True
print("7 - underground")
for test_num, test in enumerate(test_case):
    result = test.run(sol)
    text_result = "Pass" if result else "Fail"
    print(f"Test {test_num + 1} - {text_result}")
    overall_result = overall_result and result
text_overall_result = "Accepted" if overall_result else "Rejected"
print(f"-------\nResult: {text_overall_result}\n")