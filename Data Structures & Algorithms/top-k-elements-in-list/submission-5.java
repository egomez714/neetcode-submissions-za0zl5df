class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> count = new HashMap<>();

        // 1 : 1
        // 2 : 2
        // 3 : 3
        for (int i = 0; i < nums.length; i++){
            count.put(nums[i],count.getOrDefault(nums[i],0) + 1);
        }

        List<Integer>[] bucket = new ArrayList[nums.length + 1];

        for (int index = 0; index < bucket.length; index++){
            bucket[index] = new ArrayList<>();
        }
        //  1 2 3 4
        //  
        
        for (Map.Entry<Integer,Integer> bucketCheck : count.entrySet()){
            bucket[bucketCheck.getValue()].add(bucketCheck.getKey());
        }
        int [] answer = new int[k];
        int index = 0;
        for (int i = bucket.length -1; i >= 0 && index < k; --i){
            for(int ans : bucket[i]){
                if (index == k) return answer;
                answer[index++] = ans;
            }
        }
        return answer;
    }
}
