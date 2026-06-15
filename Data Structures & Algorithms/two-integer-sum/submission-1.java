class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> mapping = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            mapping.put(nums[i], i);
        }
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (mapping.containsKey(complement) && i!= mapping.get(complement)) {
                return new int[] {i, mapping.get(complement)};
            }
        }

        return new int[] {1, 1};
    }
}
