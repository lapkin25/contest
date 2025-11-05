from sol_underground import sol_underground

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


test_case = [test_1, test_2, test_3]
sol = Solution(sol_underground)
overall_result = True
for test_num, test in enumerate(test_case):
    result = test.run(sol)
    text_result = "Pass" if result else "Fail"
    print(f"Test {test_num + 1} - {text_result}")
    overall_result = overall_result and result
text_overall_result = "Accepted" if overall_result else "Rejected"
print(f"-------\nResult: {text_overall_result}")
