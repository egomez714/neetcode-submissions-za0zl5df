class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> count = new HashMap<>();

        for(int index = 0; index < nums.length; index++){
            count.put(nums[index],count.getOrDefault(nums[index],0) + 1);
        }

        List<Integer>[] bucketArr = new List[nums.length + 1];
        for(int index = 0; index < bucketArr.length; index++){
            bucketArr[index] = new ArrayList();
        }
        for(Map.Entry<Integer,Integer> mapIterate : count.entrySet()){
            bucketArr[mapIterate.getValue()].add(mapIterate.getKey());
        }
        
        int pos = 0;
        int[] answer = new int[k];

        for(int index = bucketArr.length - 1; index > 0; index--){
            for (int num : bucketArr[index]){
                answer[pos++] = num;
                if (pos == k) return answer;
            }
        } 
        return answer;
    }
}
