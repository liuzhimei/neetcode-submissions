class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        result = 0
        people.sort() # sort people in increasing order
        l, r = 0, len(people)-1
        while l < r:
            if people[l] == limit:
                result += 1
                l += 1
            elif people[r] == limit:
                result += 1
                r -= 1
            elif people[l] + people[r] <= limit:
                result += 1
                l += 1
                r -= 1
            elif people[l] + people[r] > limit:
                result += 1
                r -= 1
        if l == r:
            result += 1
        return result
