# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        heapsize = 0
        ptrs = []
        for i, lst in enumerate(lists):
            if lst:
                heap.append(dict(val=lst.val, idx=i))
                heapsize += 1
                ptrs.append(lst)
            else:
                ptrs.append(lst)

        for i in range(heapsize - 1, -1, -1):
            self.min_heapify(heap, heapsize, i)

        mptr = head = ListNode(None)
        while heapsize > 0:
            idx = heap[0]['idx']
            mptr.next = ptrs[idx]
            mptr = mptr.next
            ptrs[idx] = ptrs[idx].next
            if ptrs[idx]:
                heap[0] = dict(val=ptrs[idx].val, idx=idx)
            else:
                heapsize -= 1
                heap[0] = heap[heapsize]
            self.min_heapify(heap, heapsize, 0)

        return head.next

    def min_heapify(self, heap, heapsize, i):
        if 2 * i + 1 < heapsize and heap[2 * i + 1]['val'] < heap[i]['val']:
            smallest = 2 * i + 1
        else:
            smallest = i
        if 2 * i + 2 < heapsize and heap[2 * i
                                         + 2]['val'] < heap[smallest]['val']:
            smallest = 2 * i + 2
        if smallest != i:
            heap[smallest], heap[i] = heap[i], heap[smallest]
            self.min_heapify(heap, heapsize, smallest)
