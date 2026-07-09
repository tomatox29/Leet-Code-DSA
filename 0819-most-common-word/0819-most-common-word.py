from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub(r"[^\w\s]", " ", paragraph.lower()).split()
        count = Counter(word for word in words if word not in banned)
        return max(count,key=count.get)