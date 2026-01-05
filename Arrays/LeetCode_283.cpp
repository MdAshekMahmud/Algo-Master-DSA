// Move Zeroes
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int> &nums) {
        int n = nums.size();
        int len = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) {
                swap(nums[len], nums[i]);
                len++;
            }
        }
        return;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    Solution s;
    vector<int> nums = {0, 1, 0, 3, 12};
    s.moveZeroes(nums);

    return 0;
}