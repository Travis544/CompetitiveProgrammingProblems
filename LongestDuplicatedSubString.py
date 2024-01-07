from collections import defaultdict
from operator import itemgetter

class Solution:
# #code to build suffix array, kasai algorithm to find lcp
# LCP Array is an array of size n (like Suffix Array). A value lcp[i] indicates length of the longest common prefix of the suffixes indexed by suffix[i] and suffix[i+1].
# Suffix[i] index into suffix array.
    def kasai(self, s, sa):
        n = len(sa)
        rank = [0] * n
        for i in range(n):
            rank[sa[i]] = i
        lcp = [0] * n
        k = 0
        for i in range(n):
            if rank[i] == n - 1:
                k = 0
                continue
            j = sa[rank[i] + 1]
            while j + k < n and i + k < n and s[i + k] == s[j + k]:
                k += 1
            lcp[rank[i]] = k
            k = max(0, k - 1)
        return lcp

    def manber_myers(self, s, buckets, order=1):
        d = defaultdict(list)
        for bucket in buckets:
            d[s[bucket:bucket+order]].append(bucket)

        res = []
        # d.items return  a list of tuple with key and value.
        for k, v in sorted(d.items()):
            if len(v) > 1:
                # if two or more suffix start with the same character of order 1, recursively sort them with
            # by looking at *2 more characters of the suffix bucket
                res.extend(self.manber_myers(s, v, order * 2))
            else:
                res.append(v[0])
        return res

    def longestDupSubstring(self, s: str) -> str:
        sa = self.manber_myers(s, range(len(s)), 1)
        lcp = self.kasai(s, sa)
        if not any(lcp):
            return ""

        # find the pair of suffixes with the longest common prefix and get that substring-->from the start suffix to end with however long the prefix is matched with the i+1 suffix.
        pos, length = max(enumerate(lcp), key=itemgetter(1))
        return s[sa[pos] : sa[pos] + length]

so=Solution()
s="ababba$"
print(so.manber_myers(s, range(len(s)), 1))
