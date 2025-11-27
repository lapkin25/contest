if __name__ == "__main__":
    import sys
    sys.path.append('..')
    from config import root_contestant
    sys.path.append('../' + root_contestant + '/3 - detox')

from sol_detox import sol_detox as sol_contestant
#from sol_jury_detox import sol_detox as sol_contestant
from sol_jury_detox import sol_detox as sol_jury


class Solution:
    def __init__(self, run_callback):
        self.run_callback = run_callback

def check_output(input, output, answer):
    if len(output) != len(answer):
        return False
    return set(output) == set(answer)

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
a, b, c = 50, 30, 900
ans = [(0, 30), (3, 25), (6, 20), (9, 15), (12, 10), (15, 5), (18, 0)]
test_1 = UnitTest_GivenAnswer((a, b, c), ans)

# Тест 2
a, b, c = 12, 16, 1333
ans = []
test_2 = UnitTest_GivenAnswer((a, b, c), ans)

sol_etalon = Solution(sol_jury)

# Остальные тесты
abc_values = [(1, 1, 1), (1, 1, 10), (1, 1, 100000), (100000, 100000, 100000),
              (2, 2, 2), (2, 2, 10), (9, 5, 99), (100000, 1, 1), (1, 3, 100000),
              (50, 70, 29876), (76, 42, 12345), (300, 500, 100000), (77, 333, 11725)]
tests = [UnitTest_JuryAnswer(input_data, sol_etalon) for input_data in abc_values]


test_case = [test_1, test_2] + tests
sol = Solution(sol_contestant)
overall_result = True
print("3 - detox")
for test_num, test in enumerate(test_case):
    result = test.run(sol)
    text_result = "Pass" if result else "Fail"
    print(f"Test {test_num + 1} - {text_result}")
    overall_result = overall_result and result
text_overall_result = "Accepted" if overall_result else "Rejected"
print(f"-------\nResult: {text_overall_result}\n")