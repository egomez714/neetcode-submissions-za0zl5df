class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        myMap = defaultdict(int)
        for i in range(len(numbers)):
            find = target - numbers[i]
            if myMap[find]:
                return [myMap[find],i +1]
            myMap[numbers[i]]= i + 1
        return []