class Solution {
    public int search(int[] nums, int target) {
        return bs(0, nums.length -1, nums, target);
    }

    public int bs(int l, int r, int[] nums, int target){
        if(l > r) return -1;
        int m = l + (r - l) / 2;

        if (nums[m] == target) return m;
        return (nums[m] < target) ? bs(m+1, r, nums, target): bs (l, m-1, nums, target);

    }
}
