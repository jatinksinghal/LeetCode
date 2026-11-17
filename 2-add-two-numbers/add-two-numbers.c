/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *sum=NULL;
    struct ListNode *tail=NULL;
    struct ListNode *head1=l1;
    struct ListNode *head2=l2;
    int carry=0;
    while(head1!=NULL || head2!=NULL || carry!=0){
        int a ,b;
        if(head1!=NULL){
            a=head1->val;
        }
        else a=0;
        if(head2!=NULL){
            b=head2->val;
        }
        else b=0;
        int total=a+b+carry;
        int digit=total%10;
        carry=total/10;
        struct ListNode *newnode=malloc(sizeof(struct ListNode));
        newnode->val=digit;
        newnode->next=NULL;
       
        if(sum==NULL){
            sum=newnode;
            tail=newnode;
        }
        else {
            tail->next=newnode;
            tail=newnode;
        }
        if(head1!=NULL) head1=head1->next;
        if(head2!=NULL) head2=head2->next;
    }
    return sum;
}