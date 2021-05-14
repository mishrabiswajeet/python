check=False
if num<0:
    check=True
string=str(num)
if check :
    print((string[::-1]))
    print(True,"\nTherefore it is a palindrome")
else:
    print(int(string[::-1]))
    print(False,"\nTherefore it is not a palindrome")













































# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 0
        l1 = head
        while True:
            count += 1
            if l1.next == None:
                break
            l1 = l1.next
        delete_node = count+1-n
        
        if count == 1:
            return    
        count = 0
        main = ln = ListNode()
        while True:
            count += 1
            if count == delete_node:
                if head.next == None:
                    break
                head = head.next
                continue
            ln.val = head.val
            ln.next = head.next
            if head.next == None:
                break
            head = head.next
            if head.next == None and count+1 == delete_node:
                ln.next = None
            else:
                ln = ln.next
        return main
