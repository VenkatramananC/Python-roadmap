def twoSum(nums: list[int], target: int) -> list[int]:
        if len(nums) >= 2:
            for num in len(nums):
                if nums[num] + nums[num + 1] == target:
                     return list(num,num+1)
                else:
                     continue

twoSum(nums = [2,7,11,15])
twoSum(target = 9)
print(twoSum)
