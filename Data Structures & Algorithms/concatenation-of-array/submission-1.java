class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ret = new int[2*n];
        for( int x = 0 ; x < n ; x++ ){
            ret[x] = nums[x];
            ret[x+n] = nums[x];
        }
        return ret;
    }
}