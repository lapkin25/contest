if __name__ == "__main__":
    import sys
    sys.path.append('..')
    from config import root_contestant
    sys.path.append('../' + root_contestant + '/8 - sakura')

from sol_sakura import sol_sakura as sol_contestant
#from sol_jury_sakura import sol_sakura as sol_contestant
from sol_jury_sakura import sol_sakura as sol_jury


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

class UnitTest_JuryAnswer(UnitTest):
    def __init__(self, input, sol_etalon):
        self.input = input
        self.sol_etalon = sol_etalon
    def run(self, sol):
        output = sol.run_callback(self.input)
        answer = self.sol_etalon.run_callback(self.input)
        return check_output(self.input, output, answer)


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

sol_etalon = Solution(sol_jury)

# Тест 4
dates = ['10.04', '11.04', '12.04']
test_4 = UnitTest_JuryAnswer(dates, sol_etalon)

# Тест 5
dates = ['30.03', '28.02']
test_5 = UnitTest_JuryAnswer(dates, sol_etalon)

# Тест 6
dates = ['01.01', '31.01', '01.02', '02.01', '12.12', '31.12', '01.01']
test_6 = UnitTest_JuryAnswer(dates, sol_etalon)

# Тест 7
dates = ['01.01', '02.01', '03.01', '04.01', '02.02', '05.01', '10.03', '15.04', '30.05', '30.06', '31.07', '31.08', '30.09', '31.10', '30.11', '31.12']
test_7 = UnitTest_JuryAnswer(dates, sol_etalon)


test_case = [test_1, test_2, test_3, test_4, test_5, test_6, test_7]
sol = Solution(sol_contestant)
overall_result = True
print("8 - sakura")
for test_num, test in enumerate(test_case):
    result = test.run(sol)
    text_result = "Pass" if result else "Fail"
    print(f"Test {test_num + 1} - {text_result}")
    overall_result = overall_result and result
text_overall_result = "Accepted" if overall_result else "Rejected"
print(f"-------\nResult: {text_overall_result}\n")