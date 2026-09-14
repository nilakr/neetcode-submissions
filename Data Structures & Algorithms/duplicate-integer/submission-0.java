class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> mapping = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (!mapping.containsKey(nums[i])) {
                mapping.put(nums[i], 1);
            }
            else {
                return true;
            }
        }
        return false;

    }
}