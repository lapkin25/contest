from sol_vltokyo import sol_vltokyo

class Solution:
    def __init__(self, run_callback):
        self.run_callback = run_callback

def check_output(input, output, answer):
    if len(output) != len(answer):
        return False
    ok = True
    for i in range(len(output)):
        ok = ok and (set(output[i]) == set(answer[i]))
    return ok

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
s = ['VLADIVOSTOK', 'AVATAR']
t = ['TOKYO', 'VLADISLAV', 'VLAD', 'STOKS']
ans = [['VLAD', 'STOKS'], ['VLADISLAV']]
test_1 = UnitTest_GivenAnswer((s, t), ans)

# Тест 2
s = ['ABABACA']
t = ['ACAB', 'ACABA', 'ABACA']
ans = [['ABACA']]
test_2 = UnitTest_GivenAnswer((s, t), ans)


test_case = [test_1, test_2]
sol = Solution(sol_vltokyo)
overall_result = True
for test_num, test in enumerate(test_case):
    result = test.run(sol)
    text_result = "Pass" if result else "Fail"
    print(f"Test {test_num + 1} - {text_result}")
    overall_result = overall_result and result
text_overall_result = "Accepted" if overall_result else "Rejected"
print(f"-------\nResult: {text_overall_result}")
