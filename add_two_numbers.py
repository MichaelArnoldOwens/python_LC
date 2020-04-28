class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    head = dummy
    carry = 0
    while l1 or l2:
        if l1 and l2:
            sum = l1.val + l2.val + carry
            if sum > 9:
                sum = sum - 10
                carry = 1
            else:
                carry = 0
            next = ListNode(sum)
        elif l1:
            sum = l1.val + carry
            if sum > 9:
                sum = sum - 10
                carry = 1
            else:
                carry = 0
            next = ListNode(sum)
        elif l2:
            sum = l2.val + carry
            if sum > 9:
                sum = sum - 10
                carry = 1
            else:
                carry = 0
            next = ListNode(sum)
        dummy.next = next
        dummy = dummy.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if carry == 1:
        dummy.next = ListNode(carry)
    dummy = head.next
    while dummy:
        end = " -> "
        if not dummy.next:
            end = ""
        print(dummy.val, end = end)
        dummy = dummy.next
    return head.next

num1 = ListNode(9)
num2 = ListNode(9)
addTwoNumbers(num1, num2)
