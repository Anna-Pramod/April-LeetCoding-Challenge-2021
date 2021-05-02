#Given the head of a singly linked list, return true if it is a palindrome.
#Constraints:
#The number of nodes in the list is in the range [1, 105].
#0 <= Node.val <= 9
#Follow up: Could you do it in O(n) time and O(1) space?

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        crs = head
        n = 0
        while crs:
            n+=1
            crs = crs.next
        mid = n//2
        i = 0
        
        # Reversing a LinkedList!
        def reverse(head):
            init = None
            while (head):
                nxt = head.next
                head.next = init
                init = head
                head = nxt
            return init
        
        fst = scnd = head
        
        while i<mid:
            scnd = scnd.next
            i+=1
        scnd = reverse(scnd)
        
        while fst and scnd:
            if fst.val != scnd.val:
                return False
            fst = fst.next
            scnd = scnd.next
        return True
        
