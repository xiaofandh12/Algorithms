import java.lang.Math;

public class Solution {
    public int rob(int[] nums) {
        int size = nums.length;
        int Take = 0;
        int NonTake = 0;
        for(int i = 0; i < size; i++) {
            int temp = NonTake;
            NonTake = Math.max(Take, NonTake);
            Take = temp + nums[i];
        }
        return Math.max(Take, NonTake);
    }
    public static void main(String[] args) {
        int[] nums = {8, 3, 6, 15, 4, 9, 7, 10};//数组静态初始化
        Solution solution = new Solution();
        System.out.println(solution.rob(nums));
    }
}
