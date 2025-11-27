if __name__ == "__main__":
    import sys
    sys.path.append('..')
    from config import root_contestant
    sys.path.append('../' + root_contestant + '/4 - classify')

from sol_classify import sol_classify as sol_contestant
#from sol_jury_classify import sol_classify as sol_contestant
from sol_jury_classify import sol_classify as sol_jury

import random

class Solution:
    def __init__(self, run_callback):
        self.run_callback = run_callback

def check_output(input, output, answer):
    return output == answer

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
    def __init__(self, seed, len_train, len_test, sol_etalon):
        random.seed(seed)
        # генерируем input
        x_train = []
        y_train = []
        for i in range(len_train):
            x1 = random.random() * 1000
            x2 = random.random() * 1000
            x_train.append((x1, x2))
            y = random.choice([0, 1])
            y_train.append(y)
        x_test = []
        y_test = []
        for i in range(len_test):
            x1 = random.random() * 1000
            x2 = random.random() * 1000
            x_test.append((x1, x2))
            y = random.choice([0, 1])
            y_test.append(y)
        self.input = (x_train, y_train, x_test, y_test)
        self.sol_etalon = sol_etalon


# Тест 1
x_train = [(120, 60), (100, 60), (140, 100), (140, 80)]
y_train = [0, 0, 1, 1]
x_test = [(125, 75), (140, 60), (140, 75), (110, 75)]
y_test = [1, 1, 0, 0]
ans = [ [1, 1], [0, 2] ]
test_1 = UnitTest_GivenAnswer((x_train, y_train, x_test, y_test), ans)

sol_etalon = Solution(sol_jury)

# Тест 2
x_train = [(0, 0), (1000, 1000), (500, 500), (0, 500), (500, 0)]
y_train = [0, 0, 1, 1, 1]
x_test = [(200, 250), (0, 0), (0, 1000), (1000, 0), (500, 500), (0, 500), (500, 0)]
y_test = [1, 1, 0, 0, 0, 1, 0]
test_2 = UnitTest_JuryAnswer((x_train, y_train, x_test, y_test), sol_etalon)

# Тест 3
test_3 = UnitTest_Generator_1(1234, 100, 100, sol_etalon)

# Тест 4
test_4 = UnitTest_Generator_1(123, 10, 100, sol_etalon)

# Тест 5
test_5 = UnitTest_Generator_1(12345, 100, 35, sol_etalon)


test_case = [test_1, test_2, test_3, test_4, test_5]
sol = Solution(sol_contestant)
overall_result = True
print("4 - classify")
for test_num, test in enumerate(test_case):
    result = test.run(sol)
    text_result = "Pass" if result else "Fail"
    print(f"Test {test_num + 1} - {text_result}")
    overall_result = overall_result and result
text_overall_result = "Accepted" if overall_result else "Rejected"
print(f"-------\nResult: {text_overall_result}\n")