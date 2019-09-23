'''
@Descripttion: 
@Author: daxiong
@Date: 2019-09-21 19:11:44
@LastEditors: daxiong
@LastEditTime: 2019-09-21 19:52:21
'''
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int> &nums) {
        if(nums.empty())
            return nullptr;
        return recursive(nums,0,nums.size()-1);
    }

    TreeNode* recursive(vector<int> &nums, int begin, int end){
        if(begin > end)
            return nullptr;
        int mid = (begin+ end) /2;
        TreeNode *root = new TreeNode(nums[mid]);
        root->begin = recursive(nums, begin,mid -1);
        root->end = recursive(nums,mid+1, end);
        return root;
    }
};