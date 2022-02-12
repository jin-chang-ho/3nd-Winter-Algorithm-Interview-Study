class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        for stone in stones:
            freqs[stone] += 1

        for jewel in jewels:
            if jewel in freqs:
                count += freqs[jewel]

        return count
        
        