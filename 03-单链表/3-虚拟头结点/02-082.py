# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def list_to_list_node(l):
    p = head = ListNode(-1)
    for v in l:
        p.next = ListNode(v)
        p = p.next
    return head.next


def list_node_to_list(list_node):
    l = []
    while list_node:
        l.append(list_node.val)
        list_node = list_node.next
    return l


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = ListNode(-1)
        start.next = head
        p = start
        while p.next and p.next.next:
            if p.next.val == p.next.next.val:
                q = p.next.next
                # if q.next is None:
                #     p.next = None
                #     break
                while q.next is not None and q.next.val == p.next.val:
                    q = q.next
                p.next = q.next
            else:
                p = p.next
        return start.next





if __name__ == '__main__':
    obj = Solution()
    while True:
        l1_str = input().strip()
        l1 = list(map(int, l1_str.split()))
        l1 = list_to_list_node(l1)
        # val = int(input().strip())
        res_node = obj.deleteDuplicates(l1)
        res = list_node_to_list(res_node)
        print(res)
