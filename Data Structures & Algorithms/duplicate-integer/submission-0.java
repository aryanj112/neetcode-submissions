class Solution {
    public boolean hasDuplicate(int[] nums) {
        boolean output = false;
        for(int i = 0; i < nums.length; i++){
            int numCurr = nums[i];
            for(int j = 0; j < nums.length; j++){
                if(nums[j] == numCurr & i != j){
                    output = true;
                }

            }
        }
        return output;
    }
}
