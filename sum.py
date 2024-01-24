def sum_of_two(nums , target):
    num_indices = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_indices:
            return [num_indices[complement],i]
        
        else:
            num_indices[num] = i
    return None

# nums = list(map(int,input("Enter two numbers: ").split()))
nums = [4,6,8,14]
target = 14
result = sum_of_two(nums , target)
print(result)