import sys
sys.setrecursionlimit(1000000)

class node(object):
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def print_ll(head):
    while head is not None:
        print(str(head.val) + " -> ", end='') if head.next is not None else print(str(head.val))
        head = head.next

def reverse_ll(current, prev=None):
    # Case 1: at the end
    if prev is not None and current is None:
        return prev # as new head

    # Case 2: single node
    if prev is None and current.next is None:
        return current

    # Case 3: at the head
    if prev is None and current is not None and current.next is not None:
        pass_cur = current.next
        current.next = None
        return reverse_ll(pass_cur, current)

    # Case 4: middle
    pass_cur = current.next
    current.next = prev
    return reverse_ll(pass_cur, current)

head = node(0, None)
for i in range(1,90000):
    new_nd = node(i, None)
    cur = head if i==1 else cur.next
    cur.next = new_nd
    tail = new_nd

print_ll(reverse_ll(head, None))

