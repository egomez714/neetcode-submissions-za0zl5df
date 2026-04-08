class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> count = new HashMap<>();

        for(int i = 0; i < nums.length; i++){

            int newTarget = target - nums[i];

            if (count.containsKey(newTarget)){
                return new int[]{count.get(newTarget),i};
            }
            else{
                count.put(nums[i],i);
            }
        }
        return new int[]{};
    
    }
}
