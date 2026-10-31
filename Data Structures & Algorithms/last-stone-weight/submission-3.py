class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heapify the list to a max heap
        neg_stones = [-x for x in stones]
        heapq.heapify(neg_stones)
        while len(neg_stones) > 1:
            x = - heapq.heappop(neg_stones)
            y = - heapq.heappop(neg_stones)
            if x == y:
                continue
            else:
                heapq.heappush(neg_stones, y - x)
        if neg_stones:
            return - neg_stones[0]
        else:
            return 0