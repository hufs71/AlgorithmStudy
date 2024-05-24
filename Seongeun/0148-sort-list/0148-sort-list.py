# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      dummy = ListNode(0)
      dummy.next = head

      # Grab sublists of size 1, then 2, then 4, etc, until fully merged
      steps = 1
      while True:
        # Record the progress of the current pass into a single semi sorted list by updating
        # the next of the previous node (or the dummy on the first loop)
        prev = dummy

        # Keep track of how much is left to process on this pass of the list
        remaining = prev.next

        # While the current pass though the list has not been completed
        num_loops = 0
        while remaining:
          num_loops += 1

          # Split 2 sublists of steps length from the front
          sublists = [None, None]
          sublists_tail = [None, None]
          for i in range(2):
            sublists[i] = remaining
            substeps = steps
            while substeps and remaining:
              substeps -= 1
              sublists_tail[i] = remaining
              remaining = remaining.next
            # Ensure the subslist (if one was made) is terminated
            if sublists_tail[i]:
              sublists_tail[i].next = None

          # We have two sublists of (upto) length step that are sorted, merge them onto 
          # the end into a single list of (upto) step * 2
          while sublists[0] and sublists[1]:
            if sublists[0].val <= sublists[1].val:
              prev.next = sublists[0]
              sublists[0] = sublists[0].next
            else:
              prev.next = sublists[1]
              sublists[1] = sublists[1].next
            prev = prev.next

          # One list has been finished, attach what ever is left of the other to the end
          if sublists[0]:
            prev.next = sublists[0]
            prev = sublists_tail[0]
          else:
            prev.next = sublists[1]
            prev = sublists_tail[1]

        # Double the steps each go around
        steps *= 2

        # If the entire list was fully processed in a single loop, it means we've completely sorted the list and are done
        if 1 >= num_loops:
          return dummy.next