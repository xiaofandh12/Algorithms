#include <vector>
#include <iostream>
using namespace std;

//mac下编译命令: sudo gcc -o Solution.out Solution.cc -lstdc++
class Solution {
    public:
        vector<int> countBits(int num) {
            vector<int> ans(num+1, 0);
            for (int i = 0; i <= num; ++i) {
                ans[i] = ans[i/2] + (i%2);
            }
            return ans;
        }
};

int main() {
    Solution solution;
    int num = 10;
    vector<int> ans(num+1,0);
    ans = solution.countBits(num);
    vector<int>::iterator it;
    //将结果以列表的形式输出
    cout << "[";
    for (it = ans.begin(); it != ans.end();) {
        cout << (*it);
        //这样做是为了不让在打印输出ans时，其最后一个元素后有空格
        it++;
        if (it != ans.end()) {
            cout << " ";
        }
    }
    cout << "]" << endl;
}
