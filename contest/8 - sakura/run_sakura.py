from sol_sakura import sol_sakura

class Solution:
    def __init__(self, run_callback):
        self.run_callback = run_callback

def check_output(input, output, answer):
    if len(output) != len(answer):
        return False
    for i in range(len(output)):
        if output[i] != answer[i]:
            return False
    return True

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
dates = ['15.04', '10.04', '05.04', '12.04', '20.04']
ans = [['15.04', '10.04', '05.04'], ['05.04', '12.04', '20.04']]
test_1 = UnitTest_GivenAnswer(dates, ans)

# Тест 2
dates = ['15.04', '10.04', '12.04', '14.04', '12.04']
ans = [['15.04', '10.04'], ['10.04', '12.04', '14.04'], ['14.04', '12.04']]
test_2 = UnitTest_GivenAnswer(dates, ans)

# Тест 3
dates = ['10.04', '15.04', '20.04']
ans = [['10.04', '15.04', '20.04']]
test_3 = UnitTest_GivenAnswer(dates, ans)


test_case = [test_1, test_2, test_3]
sol = Solution(sol_sakura)
overall_result = True
for test_num, test in enumerate(test_case):
    result = test.run(sol)
    text_result = "Pass" if result else "Fail"
    print(f"Test {test_num + 1} - {text_result}")
    overall_result = overall_result and result
text_overall_result = "Accepted" if overall_result else "Rejected"
print(f"-------\nResult: {text_overall_result}")
