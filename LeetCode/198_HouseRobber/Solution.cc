//编译: sudo gcc Solution.cc -lstdc++
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int size = nums.size();
        int NonTake = 0;
        int Take = 0;
        for (int i = 0; i < size; i++) {
            int temp = NonTake;
            NonTake = max(NonTake, Take);
            Take = temp + nums[i];
        }
        return max(NonTake, Take);
    }
};

int main() {
    Solution *solution = new Solution();

    //用一个nums_bak来初始化nums
    int nums_bak[8] = {8, 3, 6, 15, 4, 9, 7, 10};
    vector<int> nums(nums_bak, nums_bak+8);
    
    cout << solution->rob(nums) << endl;
}
/* main函数也可以写成下面这样
 * 如果写成Solution solution = new Solution();则程序就会报错.
 * Solution *solution = new Solution();是在堆栈中创建Solution类型的变量并用指向Solution类变量的指针指向它。
 * Solution solution;是创建Solution类型的变量
 *
 * int main() {
 *  Solution solution;
 *
 *  int nums_bak[8] = {8, 3, 6, 15, 4, 9, 7, 10);
 *  vector<int> nums(nums_bak, nums_bak+8);
 *
 *  cout << solution->rob(nums) << endl;
 */  
