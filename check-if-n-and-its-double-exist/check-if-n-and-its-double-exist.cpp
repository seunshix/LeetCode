class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_map<int, bool> map;
        
        for (int i = 0; i < size(arr); i++){
            if (map[arr[i] * 2] == 1 || (map[arr[i]/2]==1&& arr[i]%2==0) ){
                    return true;
            }
            map[arr[i]] = 1;
        }        
                
        return false;
    }
};