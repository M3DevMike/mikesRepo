numbers = list(range(0,101))
revNum = list(reversed(range(0,101)))

def missing_no(nums):
    
    removedNum = nums.remove(35)
    nums.sort()
    missingNum = []
    for number in range(nums[0], nums[-1]+1):
        if number not in nums:
            missingNum.append(number)
    for missNum in missingNum:
        print(missNum)
        
missing_no(revNum)