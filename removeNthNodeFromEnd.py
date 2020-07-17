#Leet Code Challenge

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 1 #list starts at one because there will always be at least one node. 
        p = head #previous pointer
        cur = head #current pointer
        while cur.next: #while a next node exists
            size += 1 #increment the size
            cur = cur.next #move the current node over one
            if size > n + 1: # if size becomes greater than the index of the node to be taken from the end
                p = p.next #assign th previous pointer to the next node
        if size == n: #edge case if there is only two values in the list
            return head.next #return the next node in the list
        else:
            p.next = p.next.next #deletes the node from the desired index
            return head #return head of the list
