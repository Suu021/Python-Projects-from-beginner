def solution(roman):
    """complete the solution by transforming the roman numeral into an integer"""
    sum = 0
    min_num = 1000
    dict_roman = {"I": "1",
                  "V": "5",
                  "X": "10",
                  "L": "50",
                  "C": "100",
                  "D": "500",
                  "M": "1000"}
    s_roman = roman.strip()  # To take off the excess space
    l_roman = list(s_roman)  # To do a list of roman numbers
    t_roman = [int(i.replace(i.upper(), dict_roman[i.upper()])) for i in l_roman]  # To translate the list of roman
    # numbers into list of integers
    min_v = min(t_roman)  # To search the minimum value
    if t_roman[-1] == min(t_roman):  # if the minimum value is the last item of
        # the string the code will just sum all of them
        for i in t_roman:
            if 1 < i < min_num:  # verify if it's a decreasing list or if there is a larger number in front of a
                # smaller one
                min_num = i
            elif i > min_num != min_v:  # if there is a larger number in front of a smaller one, this double of
                # smaller will be discounted of the sum
                sum -= min_num * 2
            sum += i
        return sum
    else:  # else, the total will be: the sum - double of the count of the minimum value
        for i in t_roman:
            if 1 < i < min_num:  # Same function as line 21
                min_num = i
            elif i > min_num != min_v:
                sum -= min_num * 2  # Same function as line 23
            sum += i
        double = min_v * 2
        total = sum - double
        return total


print(f'2240 = {solution("MMCCXL")}\n')
print(f'291 = {solution("CCXCI")}\n')
print(f'2641 = {solution("MMDCXLI")}\n')
print(f'2747 = {solution("MMDCCXLVII")}\n')
print(f'1982 = {solution("MCMLXXXII")}\n')
print(f'20 = {solution("XX")}\n')
print(f'18 = {solution("XVIII")}')