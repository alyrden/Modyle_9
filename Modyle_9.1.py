
def apply_all_func(int_list, *functions):
    result = {}

    for i in functions:
        result[i.__name__] = i(int_list)
    return result
    print(result)

def min(int_list):
    if not int_list:
        raise ValueError("Список пуст")
    min = int_list[0]
    for i in int_list:
        if i < min:
            min = i
    return min

def max(int_list):
    if not int_list:
        raise ValueError("Список пуст")
    max = int_list[0]
    for i in int_list:
        if i > max:
            max = i
    return max

def len(int_list):
    count =0
    for i in int_list:
        count += 1
    return count

def sum(int_list):
    total = 0
    for i in int_list:
        total += i
    return total

def sorted(int_list):
    new_list = int_list[:]
    for i in range(len(new_list)):
        for j in range(len(new_list) - i - 1):
            if new_list[j] > new_list[j + 1]:
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
    return new_list



print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))