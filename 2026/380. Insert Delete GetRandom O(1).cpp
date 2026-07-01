#include <vector>
#include <unordered_map>
using namespace std;


class RandomizedSet {
    vector<int> arr;
        unordered_map<int,int> data_struct;
public:
    RandomizedSet() {
        
        
    }
    
    bool insert(int val) {

        if(data_struct.find(val)!=data_struct.end()){ //check if element already exists
        return false;
    }
    arr.push_back(val);
    int index=arr.size()-1;
    this->data_struct.insert({val,index});
    return true;
        
    }
    
    bool remove(int val) {
         if(data_struct.find(val)==data_struct.end()){ //check if it exists
        return false;
    }
    int index_to_remove=this->data_struct[val];
    int value_moving=this->arr[arr.size()-1];

    arr[index_to_remove]=arr.back(); //replace the value to delete with last element
    arr.pop_back(); //remove the last element which is the delete value

    this->data_struct[value_moving]=index_to_remove; //update map
    this->data_struct.erase(val); //remove from map the value entirely


    return true;

        
    }
    
    int getRandom() {
         int randint=rand() % (this->arr.size());
    return arr[randint];

        
    }
};
