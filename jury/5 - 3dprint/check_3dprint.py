if __name__ == "__main__":
    import sys
    sys.path.append('..')
    from config import root_contestant
    sys.path.append('../' + root_contestant + '/5 - 3dprint')

from sol_3dprint import sol_3dprint as sol_contestant
#from sol_jury_3dprint import sol_3dprint as sol_contestant
from sol_jury_3dprint import sol_3dprint as sol_jury


class Solution:
    def __init__(self, run_callback):
        self.run_callback = run_callback

def check_output(input, output, answer):
    return abs(output - answer) < 0.01

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
a, b = 1.6, 1.4
ans = 1.711
test_1 = UnitTest_GivenAnswer((a, b), ans)

sol_etalon = Solution(sol_jury)

# Остальные тесты
values = [(1, 1.1), (0.5, 1.5), (2, 2), (5, 5), (10, 10)]
tests = [UnitTest_JuryAnswer(input_data, sol_etalon) for input_data in values]


test_case = [test_1] + tests
sol = Solution(sol_contestant)
overall_result = True
print("5 - 3dprint")
for test_num, test in enumerate(test_case):
    result = test.run(sol)
    text_result = "Pass" if result else "Fail"
    print(f"Test {test_num + 1} - {text_result}")
    overall_result = overall_result and result
text_overall_result = "Accepted" if overall_result else "Rejected"
print(f"-------\nResult: {text_overall_result}\n")
