from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0]) # sort in place

    merged = [intervals[0]]

    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]: # there is an overlap
            merged[-1][1] = max(merged[-1][1], interval[1]) # merge
        else:
            merged.append(interval) # no overlap, add to merged list

    return merged
