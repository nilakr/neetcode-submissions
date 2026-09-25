class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> twosum = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            twosum.put(nums[i], i);
        }

        for (int i = 0; i < twosum.size(); i++) {
            int val = target - nums[i];
            if (twosum.containsKey(val)) {
                int[] indices = {i, twosum.get(val)};
                return indices;
            }
        }
        return new int[] {0, 0};
    }
}
