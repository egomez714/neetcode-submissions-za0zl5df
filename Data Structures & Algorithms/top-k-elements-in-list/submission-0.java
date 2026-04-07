class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        Map <Integer, Integer> map = new HashMap<>();
        int max = 0;

        for (int i = 0; i < nums.length; ++i){
            map.put(nums[i], map.getOrDefault(nums[i],0) + 1);
        }

        List<Integer>[] bucket = new List[nums.length + 1];

        for(int i = 0; i <= nums.length; ++i){
            bucket[i] = new ArrayList<>();
        }

        for (int num : map.keySet()){
            int freq = map.get(num);
            bucket[freq].add(num);
        }
        int[] ans = new int[k];
        int index = 0;
        for (int i = bucket.length - 1; i >= 0 && index < k; i--) {
            for (int num : bucket[i]) {
                ans[index++] = num;
                if (index == k) break;
            }
        }
        return ans;
    }
}
