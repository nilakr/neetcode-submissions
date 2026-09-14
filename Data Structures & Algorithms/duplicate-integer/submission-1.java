class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> numValues = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (!numValues.containsKey(nums[i])) {
                numValues.put(nums[i], 1);
            }
            else {
                numValues.put(nums[i],      
                numValues.get(nums[i]) + 1);
            }

        }

        for (int i = 0; i < nums.length; i++) {
            if (numValues.get(nums[i]) != 1) {
                return true;
            }
        }
        return false;
    }
}