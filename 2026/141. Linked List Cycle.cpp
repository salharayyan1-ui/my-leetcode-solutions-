#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
 struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
    unordered_map<ListNode*,int> visited_nodes;
    
public:
    bool hasCycle(ListNode *head) {
        ListNode* temp=head;
        while(temp!=nullptr){
            if (this->visited_nodes.find(temp)==this->visited_nodes.end()){
                this->visited_nodes[temp]=temp->val;
            }
            else{
                return true;
            }
            temp=temp->next;
        }
        return false;

        
    }
};