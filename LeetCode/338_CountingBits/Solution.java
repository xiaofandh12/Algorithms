import java.util.Arrays;

public class Solution {
    public int[] countBits(int num) {
        int[] ans = new int[num+1];
        for (int i = 0; i <= num; i++) {
            ans[i] = 0;
        }
        for (int i = 0; i <= num; i++) {
            ans[i] = ans[i/2] + (i%2);
        }
        return ans;
    }

    public static void main(String[] args) {
        int[] ans = new int[10];
        Solution solution = new Solution();
        ans = solution.countBits(10);
        System.out.println(Arrays.toString(ans));//打印数组
    }
}

