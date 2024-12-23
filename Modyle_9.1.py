from ctypes import HRESULT


def apply_all_func(self, int_list, *functions):
    result = {}
    for i in functions:
        result[i.__name__] = i(int_list)
    return result


def min(lst):
    if not lst:
        raise ValueError("Список пуст")
    min = lst[0]
    for i in min:
        if i <= min:
            min = i
            return min

def max(list):
    if not list:
        raise ValueError("Список пуст")
    max = 0
    for i in max:
        if i >= max:
            max = i
            return max

def len(list):
    count =0
    for i in list:
        count += 1
        return count

def sum(list):
    total = 0
    for i in list:
        total += i
        return total

def sorted(list):
    new_list = list[:]
    for i in range(len(new_list)):
        for j in range(len(new_list) - i - 1):
            if new_list[j] > new_list[j + 1]:
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
    return new_list



print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))