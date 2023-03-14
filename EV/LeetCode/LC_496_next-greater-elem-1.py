'''
    runtime: 41 ms Beats 97.7%
    memory: 14.1 MB Beats 92.74%
'''

def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    stack = []
    next_greater = {}
    
    for num in nums2:
        while stack and num > stack[-1]:
            next_greater[stack.pop()] = num
        stack.append(num)
    
    result = []

    for num in nums1:
        if num in next_greater:
            result.append(next_greater[num])
        else:
            result.append(-1)
    return result
