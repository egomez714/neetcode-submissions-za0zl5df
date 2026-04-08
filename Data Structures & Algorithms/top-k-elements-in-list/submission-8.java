class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        // key : value
        // 1 : 1
        // 2 : 2

        // create a bucket with size of nums arr + 1
        // initlize each index for bucket
        // add value as index in bucket and key as value for the index

        // min heap, reverse arr and add to a new arr up to k size

        Map<Integer, Integer> frequentCounter = new HashMap<>();
        List<Integer>[] bucket = new ArrayList[nums.length + 1];
        for(int i = 0; i < bucket.length; i++){
            bucket[i] = new ArrayList<>();
        }
        for (int i = 0; i < nums.length; i++){
            frequentCounter.put(nums[i],frequentCounter.getOrDefault(nums[i],0) + 1);
        }

        for (Map.Entry<Integer,Integer> index : frequentCounter.entrySet()){
            bucket[index.getValue()].add(index.getKey());
        }

        int[] ans = new int[k];
        int pos = 0;
        for (int i = bucket.length - 1; i >= 0; i--){
            for (int num : bucket[i]) {
                if (pos == k) return ans;
                else{
                    ans[pos++] = num;
                }
            }
        }
        return ans;
    }
}
