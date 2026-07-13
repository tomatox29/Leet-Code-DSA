class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_count = 0

        for sentence in sentences:
            count = 0

            for ch in sentence:
                if ch == " ":
                    count += 1

            max_count = max(max_count, count + 1)

        return max_count