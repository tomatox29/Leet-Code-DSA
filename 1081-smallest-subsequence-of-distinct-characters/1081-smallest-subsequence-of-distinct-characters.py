class Solution:
    def smallestSubsequence(self, s: str):
        last = {ch: i for i, ch in enumerate(s)}
        stack = []
        visited = set()
        for i, ch in enumerate(s):
            if ch in visited:
                continue 
            while (
                stack and 
                stack[-1]> ch and 
                last[stack[-1]]>i
            ):
                removed=stack.pop()
                visited.remove(removed)

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)


 