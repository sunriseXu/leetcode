class Trie(object):

    def __init__(self):
        self.database = dict()
        self.flag = '-'

    def insert(self, word):
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
        for i in word:
            if i not in note:
                return False
            note = note[i]
        return self.flag in note

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        note = self.database
        for i in prefix:
            if i not in note:
                return False
            note = note[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)