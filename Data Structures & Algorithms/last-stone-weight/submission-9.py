class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 2:
            stones.sort()
            stones.reverse()
            if stones[0] == stones[1]:
                return 0
            if stones[1] > stones[0]:
                return stones[0] - stones[1]

        while len(stones) > 1: 
            stones.sort()
            stones.reverse()
            if stones[0] == stones[1]:
                stones.pop(0)
                stones.pop(0)
            if len(stones) > 1 and stones[0] > stones[1]:
                newstone = stones[0] - stones[1]
                stones.pop(0)
                stones.pop(0)
                stones.append(newstone)
        return stones[0] if stones else 0