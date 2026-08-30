class Solution {
    public int longestConsecutive(int[] nums) {
        
        // nums, 
        Set<Integer> numSet = new HashSet<>();
        // store all values in 
        for(int num : nums){
            numSet.add(num);
        }
        int longestLen = 0;
        // only starts counting len if it's a start of a seq(num-1 does not exist)
        for(int num : numSet){
            if(!numSet.contains(num-1)){
                int count = 1;
                while (numSet.contains(num + count)){
                    count ++;
                }
                longestLen = Math.max(longestLen, count);
            }
        }
        return longestLen;
    }
}
