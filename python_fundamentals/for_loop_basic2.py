list = [-1, 3, 5, -5]
def biggie_size(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list
print(biggie_size(list))

list = [-1,1,1,1]
def count_positives(list):
    positive_list = []
    for i in range(len(list)):
        if list[i] > 0:
            positive_list.append(list[i])
    list[len(list)-1] = len(positive_list)
    return list
print(count_positives(list))

list = [6,3,-2]
def sum_total(list):
    sum = 0
    for v in list:
        sum += v
    return sum
print(sum_total(list))

list = [1,2,3,4]
def average(list):
    return sum_total(list)/len(list)
print(average(list))

list = [1,2,3,4]
def length(list):
    return len(list)
print(length(list))

list = [37,2,1,-9]
def minimum(list):
    if len(list) == 0:
        return False
    min_value = list[0]
    for i in list:
        if i < min_value:
            min_value = i
    return min_value
print(minimum(list))

list = [37,2,1,-9]
def maximum(list):
    if len(list) == 0:
        return False
    max_value = list[0]
    for i in list:
        if i > max_value:
            max_value = i
    return max_value
print(maximum(list))

list = [37,2,1,-9]
def ultimate_analysis(list):
    return {
        'sumTotal': sum_total(list),
        'average': average(list),
        'minimum': minimum(list),
        'maximum': maximum(list),
        'length': length(list)
    }
print(ultimate_analysis(list))

list = [37,2,1,-9]
def reverse_list(list):
    left = 0
    right = len(list) - 1
    while left < right:
        list[left], list[right] = list[right], list[left]
        left += 1
        right -= 1
    return list
print(reverse_list(list))