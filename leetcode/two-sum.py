class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        liste = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i != j):
                    if((nums[i] + nums[j]) == target):
                        liste.append(i)
                        liste.append(j)
                        return(liste)