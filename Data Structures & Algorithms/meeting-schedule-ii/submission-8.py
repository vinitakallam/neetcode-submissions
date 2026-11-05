"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        end_times = []
        intervals.sort(key=lambda interval: interval.start)

        for interval in intervals:
            start = interval.start
            end = interval.end

            if end_times and start >= end_times[0]:
                heapq.heappop(end_times)
            
            heapq.heappush(end_times, end)
        
        return len(end_times)
        