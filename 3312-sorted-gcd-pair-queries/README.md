# GCD Values of Pairs

## 📌 Approach

At first glance, generating the GCD for every possible pair seems straightforward. However, with `n` up to `10^5`, the total number of pairs becomes **O(n²)**, which is far too slow.

The key observation is that **the maximum possible GCD is limited by the maximum value in `nums`**, not by the number of pairs. Instead of iterating over every pair, we count how many pairs can have each possible GCD.

## Step 1: Frequency Array

Create a frequency array `cnt`, where:

```text
cnt[x] = number of occurrences of x in nums
```

This allows us to quickly determine how many numbers are divisible by any integer.

---

## Step 2: Count Numbers Divisible by Each Value

For every possible GCD `i`, iterate through all of its multiples:

```python
for j in range(i, m + 1, i):
```

This counts how many numbers are divisible by `i`.

If `div` numbers are divisible by `i`, then the number of possible pairs is:

```text
div × (div - 1) / 2
```

However, this counts pairs whose GCD is **at least** `i`, not **exactly** `i`.

---

## Step 3: Inclusion-Exclusion

Some of the pairs counted for `i` actually have GCD equal to `2i`, `3i`, `4i`, and so on.

To obtain the number of pairs whose GCD is **exactly** `i`, subtract the counts of all multiples of `i`.

```python
for k in range(i * 2, m + 1, i):
    gcdCount[i] -= gcdCount[k]
```

This works because we process values from **largest to smallest**, ensuring that all larger GCD counts have already been computed.

---

## Step 4: Prefix Sum

After inclusion-exclusion,

```text
gcdCount[i]
```

stores the number of pairs whose GCD is **exactly** `i`.

Convert this into a prefix sum so that:

```text
gcdCount[i]
```

represents the number of pairs whose GCD is **less than or equal to** `i`.

---

## Step 5: Answer Queries

The problem asks for the GCD at specific indices in the sorted `gcdPairs` array.

Instead of constructing the entire array, perform a binary search on the prefix sum.

The first position where

```text
prefix >= query + 1
```

gives the required GCD value.

---

# ⏱️ Complexity Analysis

- **Time Complexity:** `O(m log m + q log m)`
- **Space Complexity:** `O(m)`

---

# 💡 Key Learnings

- Frequency Array
- Counting Multiples
- Combination Formula (`n(n-1)/2`)
- Inclusion-Exclusion Principle
- Prefix Sum
- Binary Search

Instead of generating every pair, the solution counts how many pairs belong to each possible GCD value, making it efficient even for large inputs.

---

## ⭐ Personal Note

This was one of the hardest problems I've worked on. I didn't fully understand it on the first try, but by breaking the solution into small steps—frequency counting, counting multiples, inclusion-exclusion, prefix sums, and binary search—I gradually understood the reasoning behind the algorithm.

My goal isn't just to solve Hard problems, but to understand the patterns so I can recognize and apply them in future problems.
