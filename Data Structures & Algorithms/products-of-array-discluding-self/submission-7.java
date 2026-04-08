class Solution {
    public int[] productExceptSelf(int[] nums) {
        // create new array 'output' all with all indices intialized to zero
        // create prefix starting at index 0 
        // prefix = 1
        // output
        // 1 2 4 6
        // prefix = 1
        // output = prefix * nums[i]
        // prefix *= nums[i]
        int size = nums.length;
        int [] output = new int[size];
        
        output[0] = 1;
        for(int i = 1; i < size; i++){
            output[i] = output[i-1] * nums[i-1];
        }

        int postfix = 1;
        for(int i = size - 1; i >= 0; i--){
            output[i] *= postfix;
            postfix *= nums[i];
        }
        return output;
    }
}  
