class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> mapping = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            mapping.put(nums[i], i);
        }

        for (int i = 0; i < mapping.size(); i++) {
            int val = target - nums[i];
            if (mapping.containsKey(val) && i != mapping.get(val)) {
                return new int[] {i, mapping.get(val)};
            }
        }

        return new int[] {0, 0};
    }
}
