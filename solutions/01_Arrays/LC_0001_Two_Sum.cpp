// Two Sum
#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> seen; // value -> index

        for (int i = 0; i < (int)nums.size(); i++)
        {
            int complement = target - nums[i];
            if (seen.count(complement))
            {
                return {seen[complement], i};
            }
            seen[nums[i]] = i;
        }

        return {};
    }
};

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    Solution s;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = s.twoSum(nums, target);

    for (int idx : result)
    {
        cout << idx << " ";
    }
    cout << endl;

    return 0;
}