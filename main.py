# Put your function here
def decreaseElements(nums):
    result = []
    for i in nums:
        array = []
        for x in i:
            array.append(x - 1)
        result.append(array)
    return result



# testing
nums = [[96, 5, 23, 16, 45, 63],[20,106,50,27,38,15]]
print(decreaseElements(nums))