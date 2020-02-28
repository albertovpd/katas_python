def output(lst):
    start = lst[0]
    end = lst[-1]
    if start != end:
        return '{}->{}'.format(start, end)
    else:
        return str(start)

def summary_ranges(nums):
    if not nums:
        return nums
        
    group = []
    last = nums[0]
    result = []
    for num in nums:
        if num - last > 1:
            result.append(output(group))
            group = []
        group.append(num)
        last = num
    result.append(output(group))
    return result