#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
  public:
    vector<int> twoSum(vector<int> &nums, int target) {
        unordered_map<int, int> seen; // value -> index

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (seen.find(complement) != seen.end()) {
                return {seen[complement], i};
            }
            seen[nums[i]] = i;
        }
        return {}; // no solution found
    }
};

int main() {
    Solution sol;

    vector<int> nums = {2, 7, 11, 15};
    int target = 9;

    vector<int> result = sol.twoSum(nums, target);

    if (!result.empty()) {
        cout << "Indices: [" << result[0] << ", " << result[1] << "]" << endl;
        cout << "Values: " << nums[result[0]] << " + " << nums[result[1]]
             << " = " << target << endl;
    } else {
        cout << "No solution found." << endl;
    }

    return 0;
}