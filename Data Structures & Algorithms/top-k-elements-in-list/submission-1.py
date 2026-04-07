class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        # gets all counts of the list
        for num in nums:
            myDict[num] = myDict.get(num,0) + 1
        myArr = [[] for _ in range(len(nums) + 1)]
        for key,value in myDict.items():
            myArr[value].append(key)
        res = []
        for i in range(len(myArr)-1, 0, -1):
            for num in myArr[i]:
                res.append(num)
                if k == len(res):
                    return res