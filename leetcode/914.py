class Solution(object):
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        min_count = min(count.values())
        if min_count < 2: return False
        
        def gcd(a,b):
            if a < b:
                a, b = b, a
            if a % b == 0:
                return b
            else:
                return gcd(b, a%b)
        
        tmp = min_count
        for v in count.values():
            tmp = gcd(tmp, v)
            if tmp < 2:
                return False
            
        return True
