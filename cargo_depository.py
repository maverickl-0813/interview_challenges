"""
A coding problem from A****r interview.
"""


def solution(depositories: list[int]):
    minimum_days = 0
    
    # The stop condition is all numbers goes to 0 in the list.
    # Determine the minimum number (but not zero) in the current list.
    # Subtract the number with all the numbers in the list, remove 0s since we don't care about the list.
    # There's no constraints about negative numbers and non-number input. No implement for the error handling.
    # O(n)
    
    if len(depositories) == 1:
        return 1
    
    while len(depositories) != 0:
        lowest = min(vol for vol in depositories if vol != 0)
        depositories = [vol-lowest for vol in depositories]
        depositories.remove(0)
        minimum_days += 1
    
    return minimum_days


if __name__ == '__main__':
    data = [10, 20, 1, 2]
    print(solution(data))
    