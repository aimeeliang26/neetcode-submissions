class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // increasing order; search only in the section < target
        // using two pointers 
        int len = numbers.length - 1;
        int l = 0, r = len;
        while (l <= len || r >= 0 ){
            if(numbers[l] + numbers[r] > target){
                r--;
            }else if(numbers[l] + numbers[r] < target){
                l++;
            }else{
                return new int[] {l+1, r+1};
            }
        }

        return new int[0];
    }
}
