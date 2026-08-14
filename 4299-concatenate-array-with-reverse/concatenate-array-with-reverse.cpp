class Solution {
public:
    vector<int> concatWithReverse(vector<int>& nums) {
        int a = nums.size();

        for (int i = a - 1; i >= 0; i--) {
            nums.push_back(nums[i]);
        }

        return nums;
    }
};