from plumbum import cli
import pprint
from collections import deque

class MaxOverlappingIntervals(cli.Application):
    _intervals = [(9, 14), (8, 10), (12, 16), (7, 13), (10, 12)]

    def main(self):
        if list is None or len(self._intervals) is 0:
            print("List should have at least one element")
            return 1
        else:
            overlapping_intervals = self.find_max_overlapping_intervals(self._intervals)
            pprint.pprint(overlapping_intervals)

    def find_max_overlapping_intervals(self, intervals):
        # 1. separate intervals into two sets of arrivals and departures
        arrivals = set()
        departures = set()
        for start, end in intervals:
            arrivals.add(start)
            departures.add(end)

        # 2. create a dict to keep track of intervals [ time: count }
        counts = {time: 0 for time in arrivals.union(departures)}

        # 3. sort arrival and departures lists
        s_arrs = deque(sorted(arrivals))
        s_deps = deque(sorted(departures))

        # 4. iterate the arrivals, count + 1.  If departure is next, decrement count
        count = 0
        while s_arrs and s_deps:
            if s_arrs:
                arr = s_arrs.popleft()
                count = count+1

            # continue while
            while s_deps and \
                    (not s_arrs or s_deps[0] <= arr):
                dep = s_deps.popleft()
                count = count-1
                self.add_to_count(counts, dep, count)

            self.add_to_count(counts, arr, count)

        return counts

    @staticmethod
    def add_to_count(counts, time, count):
        if counts[time] < count:
            counts[time] = count
