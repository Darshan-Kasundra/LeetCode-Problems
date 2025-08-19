class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        
        for num in range(len(nums)): 

            left_over_amount = target - nums[num]
            indice1 = num

            for index in range(len(nums)):
                if not indice1 == index:
                    if left_over_amount == nums[index]:
                        indice2 = index
                        return [indice1, indice2]
                    

        
