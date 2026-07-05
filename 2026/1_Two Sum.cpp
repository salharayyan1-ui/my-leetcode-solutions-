#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
    private:
     unordered_map<int, int> map; // key: number, value: index
    
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int curr_num;
        for (int i = 0; i < nums.size(); i++) {
            curr_num=nums[i];
            int complement = target - curr_num;
            if (map.find(complement) != map.end()) {  // Check if the complement exists in the map
                return {map[complement], i}; // return the number and its index in the map
            }
            else{
                this->map[curr_num]=i;// Return the indices of the two numbers that add up to the target
            }

        
    }
    return {0,0};
}