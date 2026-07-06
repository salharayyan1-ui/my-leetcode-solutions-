/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
    unordered_map<ListNode*,int> visited_nodes;
    
public:
    ListNode* detectCycle(ListNode *head) {
        int pos=0;
        ListNode* temp=head;
        while(temp!=nullptr){
            if (this->visited_nodes.find(temp)==this->visited_nodes.end()){
                this->visited_nodes[temp]=pos;
            }
            else{
                return temp;
            }
            temp=temp->next;
        }
        return nullptr;

        
    }
};