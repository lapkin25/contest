from sol_detox import sol_detox

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


# Тест 1
a, b, c = 50, 30, 900
ans = [(0, 30), (3, 25), (6, 20), (9, 15), (12, 10), (15, 5), (18, 0)]
test_1 = UnitTest_GivenAnswer((a, b, c), ans)

# Тест 2
a, b, c = 12, 16, 1333
ans = []
test_2 = UnitTest_GivenAnswer((a, b, c), ans)


test_case = [test_1, test_2]
sol = Solution(sol_detox)
overall_result = True
for test_num, test in enumerate(test_case):
    result = test.run(sol)
    text_result = "Pass" if result else "Fail"
    print(f"Test {test_num + 1} - {text_result}")
    overall_result = overall_result and result
text_overall_result = "Accepted" if overall_result else "Rejected"
print(f"-------\nResult: {text_overall_result}")
