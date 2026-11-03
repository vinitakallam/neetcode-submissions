"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: 
            return 0
        
        intervals.sort(key=lambda interval: interval.start)

        end_times = []

        for interval in intervals:
            if end_times and interval.start >= end_times[0]:
                heapq.heappop(end_times)
            
            heapq.heappush(end_times, interval.end)

        return len(end_times)
        