class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> prevMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            int newTarget = target - nums[i];

            if (prevMap.containsKey(newTarget)){
                return new int[] { prevMap.get(newTarget), i};
            }
            prevMap.put(nums[i],i);
        }
        return new int[]{};
    }
}
