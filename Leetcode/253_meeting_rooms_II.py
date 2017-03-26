from heapq import heappush, heapreplace

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda x: x.start)
        heap = []
        for curr in intervals:
            if heap and curr.start >= heap[0]:
                heapreplace(heap, curr.end)
            else:
                heappush(heap, curr.end)
        return len(heap)
