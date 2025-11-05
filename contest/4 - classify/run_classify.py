from sol_classify import sol_classify

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


# Тест 1
x_train = [(120, 60), (100, 60), (140, 100), (140, 80)]
y_train = [0, 0, 1, 1]
x_test = [(125, 75), (140, 60), (140, 75), (110, 75)]
y_test = [1, 1, 0, 0]
ans = [ [1, 1], [0, 2] ]
test_1 = UnitTest_GivenAnswer((x_train, y_train, x_test, y_test), ans)


test_case = [test_1]
sol = Solution(sol_classify)
overall_result = True
for test_num, test in enumerate(test_case):
    result = test.run(sol)
    text_result = "Pass" if result else "Fail"
    print(f"Test {test_num + 1} - {text_result}")
    overall_result = overall_result and result
text_overall_result = "Accepted" if overall_result else "Rejected"
print(f"-------\nResult: {text_overall_result}")
