if __name__ == "__main__":
    import sys
    sys.path.append('..')
    from config import root_contestant
    sys.path.append('../' + root_contestant + '/2 - vltokyo')

from sol_vltokyo import sol_vltokyo as sol_contestant
#from sol_jury_vltokyo import sol_vltokyo as sol_contestant
from sol_jury_vltokyo import sol_vltokyo as sol_jury

import random

class Solution:
    def __init__(self, run_callback):
        self.run_callback = run_callback

def check_output(input, output, answer):
    #print("output =", output)
    #print("answer =", answer)
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

class UnitTest_JuryAnswer(UnitTest):
    def __init__(self, input, sol_etalon):
        self.input = input
        self.sol_etalon = sol_etalon
    def run(self, sol):
        output = sol.run_callback(*self.input)
        answer = self.sol_etalon.run_callback(*self.input)
        return check_output(self.input, output, answer)

class UnitTest_Generator_1(UnitTest_JuryAnswer):
    def __init__(self, seed, len_s, len_t, sol_etalon):
        # генерируем input
        s = []
        for _ in range(len_s):
            word = 'A' * 100
            s.append(word)
        t = []
        for _ in range(len_t):
            word = 'A' * 100
            t.append(word)
        self.input = (s, t)
        self.sol_etalon = sol_etalon

class UnitTest_Generator_2(UnitTest_JuryAnswer):
    def __init__(self, seed, len_s, len_t, sol_etalon):

        def random_word():
            len_word = random.choice(range(1, 101))
            word = ''
            for i in range(len_word):
                word += chr(ord('A') + random.choice(range(26)))
            return word

        random.seed(seed)
        # генерируем input
        s = []
        for _ in range(len_s):
            word = random_word()
            s.append(word)
        t = []
        for _ in range(len_t):
            word = random_word()
            t.append(word)
        self.input = (s, t)
        self.sol_etalon = sol_etalon

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

sol_etalon = Solution(sol_jury)

# Тест 3
test_3 = UnitTest_Generator_1(1234, 100, 10000, sol_etalon)

# Тест 4
s = ['AAABC', 'MNQWE', 'QWEMNQ']
t = ['AAA', 'ABC', 'MNQ', 'AAB', 'QWE']
test_4 = UnitTest_JuryAnswer((s, t), sol_etalon)

# Тест 5
s = ['AAA']
t = ['AAA']
test_5 = UnitTest_JuryAnswer((s, t), sol_etalon)

# Тест 6
s = ['AAA', 'BBB', 'CCC', 'DDD']
t = ['AAA', 'ABA', 'BAB', 'BCD', 'DCB']
test_6 = UnitTest_JuryAnswer((s, t), sol_etalon)

# Тест 7
s = ['AAA', 'BBB', 'CCC', 'DDD']
t = ['AAA', 'ABA', 'BAB', 'BCD', 'DCB']
test_7 = UnitTest_Generator_2(1234, 100, 10000, sol_etalon)

# Тест 8
s = ['AB', 'ABC', 'ABCD', 'AABCDE', 'ABCDE', 'EDCBA', 'DCBA', 'BCA', 'BA']
t = ['A', 'AB', 'ABC', 'BCA', 'BA', 'B', 'EDC']
test_8 = UnitTest_JuryAnswer((s, t), sol_etalon)

# Тест 9
s = ['AAAAAAAAAAA', 'AAAAAAABAAAAAA', 'AAAACAAAA', 'AAAAAAADAAAAAAA']
t = ['AAAAA', 'AAAAC', 'CAAAA', 'DAAAA', 'AAAAD']
test_9 = UnitTest_JuryAnswer((s, t), sol_etalon)


test_case = [test_1, test_2, test_3, test_4, test_5, test_6, test_7, test_8, test_9]
sol = Solution(sol_contestant)
overall_result = True
print("2 - vltokyo")
for test_num, test in enumerate(test_case):
    result = test.run(sol)
    text_result = "Pass" if result else "Fail"
    print(f"Test {test_num + 1} - {text_result}")
    overall_result = overall_result and result
text_overall_result = "Accepted" if overall_result else "Rejected"
print(f"-------\nResult: {text_overall_result}\n")