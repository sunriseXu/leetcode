class WordDictionary(object):

    def __init__(self):
        self.database = dict()
        self.flag = '-'

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        note = self.database
        for i in word:
            if i not in note:
                note[i] = {}
            note = note[i]
        note[self.flag] = True
        
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        note = self.database
        notes = []
        notes.append(note)
        for i in word:
            tmp = []
            if i == '.':
                for j in notes:
                    for k in j:
                        if k != self.flag:
                            tmp.append(j[k])
            else:
                for j in notes:
                    if i in j:
                        tmp.append(j[i])
            if not tmp:
                return False
            notes = tmp
        for i in notes:
            if self.flag in i:
                return True
        return False
                    
                    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)