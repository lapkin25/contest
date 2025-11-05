from sol_factorial import sol_factorial

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


test_case = [test_1, test_2, test_3, test_4]
sol = Solution(sol_factorial)
overall_result = True
for test_num, test in enumerate(test_case):
    result = test.run(sol)
    text_result = "Pass" if result else "Fail"
    print(f"Test {test_num + 1} - {text_result}")
    overall_result = overall_result and result
text_overall_result = "Accepted" if overall_result else "Rejected"
print(f"-------\nResult: {text_overall_result}")
