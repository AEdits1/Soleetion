# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur=head
        temp=None
        c=0
        if head==None or head.next==None:
            return head
        while cur:
            c+=1
            cur=cur.next
        
        cur=head
        for i in range(k%c):
            cur=head
            while cur.next and cur.next.next:
                cur=cur.next
            temp=cur.next
            temp.next=head
            cur.next=None
            head=temp
        return head