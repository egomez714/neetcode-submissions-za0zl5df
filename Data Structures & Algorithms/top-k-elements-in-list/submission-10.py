class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap use for number : count

        # initialize bucket [[] for _ in range(len(nums) + 1)]
        # add count to index of bucket append number to appropriate bucket

        # reverse bucket and return k amount
        # a bucket may have multiple numbers appended to it

        numberFreq = {}

        for num in nums:
            numberFreq[num] = numberFreq.get(num, 0) + 1

        
        bucket = [ [] for _ in range(len(nums) + 1)]

        for key, value in numberFreq.items():
            bucket[value].append(key)
        res = []
        for i in range(len(nums), -1, -1):
            for value in bucket[i]:
                if len(res) == k:
                    return res
                else:
                    res.append(value)
        return res
        