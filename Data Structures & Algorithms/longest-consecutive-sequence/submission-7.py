class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 2 20 4 10 3 4 5
        # 

        checker = set()

        for num in nums:
            checker.add(num)
        
        longestConsecutive = 0
        
        for num in nums:
            consecutive = 1
            if num-1 in checker:
                continue
            else:
                i = num + 1
                while i in checker:
                    i+= 1
                    consecutive += 1
            longestConsecutive = max(longestConsecutive,consecutive)
        return longestConsecutive
            

            