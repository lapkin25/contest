from sol_3dprint import sol_3dprint

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


# Тест 1
a, b = 1.6, 1.4
ans = 1.711
test_1 = UnitTest_GivenAnswer((a, b), ans)


test_case = [test_1]
sol = Solution(sol_3dprint)
overall_result = True
for test_num, test in enumerate(test_case):
    result = test.run(sol)
    text_result = "Pass" if result else "Fail"
    print(f"Test {test_num + 1} - {text_result}")
    overall_result = overall_result and result
text_overall_result = "Accepted" if overall_result else "Rejected"
print(f"-------\nResult: {text_overall_result}")
