from collections import deque, Counter

class Solution:
   def findSubstring(self, s: str, words: list[str]) -> list[int]:
        words_counter = Counter(words)
        words_len = len(words)
        word_len = len(words[0])
        final_list = []
        def single_slice(start):
            counter = Counter()
            word_queue = deque([], words_len)
            start_list = []
            for i in range(start, len(s), word_len):
                word = s[i:i+word_len]
                if word not in words:
                    counter.clear()
                    word_queue.clear()
                    continue
                counter[word] += 1
                word_queue.append((i, word))
                if counter == words_counter:
                    start_list.append(word_queue[0][0])
                if len(word_queue) == words_len:
                    counter[word_queue[0][1]] -= 1
            return start_list
        
        for i in range(word_len):
            final_list.extend(single_slice(i))
        return final_list


s = Solution()
res = s.findSubstring("barfoothefoobarman", ["foo","bar"])
print(res)