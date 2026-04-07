class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, root, total):
            if total == target:
                res.append(root.copy())
                return  
            if total > target or i >= len(nums):
                return
            
            root.append(nums[i])

            dfs(i, root, total + nums[i])
            root.pop()
            dfs(i + 1, root, total)

        dfs(0,[],0)
        return res

