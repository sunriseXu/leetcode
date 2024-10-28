from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        s = "ADOBECODEBANC", t = "ABC"
        """
        def counter_equal(current, target):
            for i in target:
                if i not in current or current[i] < target[i]:
                    return False
            return True
        t_counter = Counter(t)
        t_len = len(t)
        min_len = float("inf")
        res = ''
        
        start, end = 0, t_len - 1
        while end < len(s):
            sub = s[start:end+1]
            if counter_equal(Counter(sub), t_counter):
                if end - start + 1 < min_len:
                    min_len = end - start + 1
                    res = sub
                # move start point
                start += 1 
                if start >= len(s):
                    break
                while start < len(s) and s[start] not in t:
                    start += 1
                if start >= len(s):
                    break
                end = max(end, start + t_len - 1)
                if end >= len(s):
                    break
            else:
                end += 1
                while end < len(s) and s[end] not in t:
                    end += 1
                if end >= len(s):
                    break
                    
        return res
    def minWindow2(self, s, t):
        dict_counter = Counter(t)
        current_counter = Counter()
        kind = 0
        l, r = 0, 0
        ans = [-1, 0, 0]
        while r < len(s):
            c = s[r]
            current_counter[c] += 1
            if c in t and current_counter[c] == dict_counter[c]:
                kind += 1
            
            while l <= r and kind == len(dict_counter):
                cl = s[l]
                
                # record answer
                if ans[0] == -1 or ans[0] > r - l + 1:
                    ans[0] = r - l + 1
                    ans[1] = l
                    ans[2] = r
                current_counter[cl] -= 1
                if cl in t and current_counter[cl] < dict_counter[cl]:
                    kind -= 1
                l += 1
            r += 1
        if ans[0] != -1:
            return s[ans[1]:ans[2]+1]
        else:
            return ''
        
                
            
s = Solution()
res = s.minWindow2( s = "ADOBECODEBANC", t = "ABC")
print(res)