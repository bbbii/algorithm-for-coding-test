def solution(nums):
    numlist = list(set(nums))
    if len(numlist) > len(nums) // 2:
        return len(nums) // 2
    else:
        return len(numlist)