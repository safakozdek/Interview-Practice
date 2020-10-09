import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(-x[0] ** 2 - x[1] ** 2, x) for x in points]

        heap = []
        for i in range(k):
            heappush(heap, points[i])

        for i in range(k, len(points)):
            heappushpop(heap, points[i])

        return [x[1] for x in heap]
