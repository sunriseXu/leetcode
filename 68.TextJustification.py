class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
        [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ]
        greedy
        """
        output = []
        def formatLine(start, end, ifLast):
            
            charsLen = 0
            for i in range(start, end + 1):
                charsLen += len(words[i])
            spacesLen = maxWidth - charsLen
            
            if end == start:
                return words[start] + ' ' * spacesLen
            if ifLast:
                tmp = ' '.join(words[start: end+1])
                return tmp + ' ' * (maxWidth - len(tmp))
            
            if spacesLen % (end - start) > 0:
                # leftSpaceLen = int(spacesLen / (end - start)) + 1
                # rightSpaceLen = spacesLen - leftSpaceLen * (end - start - 1)
                # leftSpace = ' ' * leftSpaceLen
                # rightSpace = ' ' * rightSpaceLen
                # return leftSpace.join(words[start: end]) + rightSpace + words[end]
                # round robin
                q,r = divmod(spacesLen, end - start)
                sp = [q+(1 if j < r else 0) for j in range(end - start)]
                tmp = ''
                for i in range(end - start):
                    tmp += words[start+i] + sp[i] * ' '
                tmp += words[end]
                return tmp
            else:
                leftSpaceLen = int(spacesLen / (end - start))
                leftSpace = ' ' * leftSpaceLen
                return leftSpace.join(words[start: end+1])
                
        start = 0
        while start < len(words):
            current = len(words[start])
            i = start + 1
            isEnd = True
            while i < len(words):
                current  += len(words[i]) + 1
                if current > maxWidth:
                    end = i - 1
                    isEnd = False
                    break
                i += 1
            if isEnd:
                end = len(words) - 1
            res = formatLine(start, end, isEnd)
            start = end + 1
            output.append(res)
        return output

s = Solution()
res = s.fullJustify(words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"], maxWidth = 16)
print(res)