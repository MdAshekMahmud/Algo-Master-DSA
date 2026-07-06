// Majority Element
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int> &nums) {
        int n = nums.size();

        unordered_map<int, int> mp;

        for (int i = 0; i < n; i++) {
            mp[nums[i]]++;
        }
        int count = 0;
        for (auto el : mp) {
            if (el.second > n / 2) {
                return el.first;
            }
        }

        return 0;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    Solution s;
    vector<int> nums = {2, 2, 1, 1, 1, 2, 2};
    s.majorityElement(nums);

    return 0;
}