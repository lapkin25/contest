def str_to_date(s):
    assert(len(s) == 5)
    assert(s[2] == '.')
    day = int(s[0:2])
    month = int(s[3:5])
    return day, month

def date_greater(date1, date2):
    return date1[1] > date2[1] or date1[1] == date2[1] and date1[0] > date2[0]

def sol_sakura(dates):
    day_month = list(map(str_to_date, dates))
    assert(len(day_month) >= 2 and len(day_month) <= 100)
    ans = []
    pos = 0
    while pos < len(day_month) - 1:
        l = [ dates[pos] ]
        flag = False
        while pos < len(day_month) - 1 and date_greater(day_month[pos + 1], day_month[pos]):
            l.append(dates[pos + 1])
            flag = True
            pos += 1
        if flag:
            ans.append(l)
        l = [ dates[pos] ]
        flag = False
        while pos < len(day_month) - 1 and date_greater(day_month[pos], day_month[pos + 1]):
            l.append(dates[pos + 1])
            flag = True
            pos += 1
        if flag:
            ans.append(l)
    return ans

if __name__ == "__main__":
    # здесь задаются тестовые входные данные
    dates = ['15.04', '10.04', '05.04', '12.04', '20.04']
    ans = sol_sakura(dates)
    print(f"answer = {ans}")
