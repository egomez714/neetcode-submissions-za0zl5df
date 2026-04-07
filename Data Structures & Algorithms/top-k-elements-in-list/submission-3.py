class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1
        arr = [[] for _ in range(len(nums) + 1)]

        for key,value in hashmap.items():
            arr[value].append(key)
        ans = []
        for i in range(len(arr)-1, 0, -1):
            for num in arr[i]:
                if k == 0:
                    return ans
                ans.append(num)
                k-=1
        return ans
