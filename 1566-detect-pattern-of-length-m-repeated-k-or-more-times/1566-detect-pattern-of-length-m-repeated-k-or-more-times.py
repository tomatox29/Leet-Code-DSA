class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:

        n = len(arr)  # Total number of elements in the array

        # We need m*k consecutive elements to form k blocks of size m.
        # So we only check starting indices where these m*k elements can fit.
        # Last valid starting index = n - (m*k)
        # Since range() excludes the last value, we use +1.
        for i in range(n - m * k + 1):

            # Take the first block of length m as the pattern
            pattern = arr[i:i + m]

            # We already have one occurrence of the pattern
            count = 1

            # Compare the next blocks with the original pattern
            while arr[i + count * m : i + (count + 1) * m] == pattern:

                # If the block matches, increase the repetition count
                count += 1

                # If the pattern repeats k times, return True
                if count == k:
                    return True

        # No valid pattern found
        return False