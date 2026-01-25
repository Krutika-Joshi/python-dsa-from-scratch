# TC: O(n)
# SC: O(n)

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for i in nums:
            ans.append(i)

        for i in nums:
            ans.append(i)
        
        return ans 

        # return nums + nums
        