from typing import List

def find_lack_numbers(numbers: List[int], range: int = None) -> List[int]:
    numbers.sort()
    if range is None: range = numbers[-1]
    data = []
    curr_num = numbers.pop(0)

    if curr_num > 1:
        between = curr_num - 1
        while between >= 1:
            data.append(between)
            between -= 1

    while numbers:
        if (numbers[0] - curr_num == 1):
            curr_num = numbers.pop(0)
        else:
            between = curr_num + 1
            while between < numbers[0]:
                data.append(between)
                between += 1
            curr_num = numbers.pop(0)

    if curr_num < range:
        between = curr_num + 1
        while between <= range:
            data.append(between)
            between += 1
    return data

if __name__ == '__main__':
    print(find_lack_numbers([2, 3, 7, 4, 9], 10))
