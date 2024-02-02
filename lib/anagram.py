# your code goes here!
class Anagram:
    pass
    def __init__(self, word):
        self.word = word
    
    # def getWord(self):
    #     return self._word
    
    # def setWord(self, word):
    #      self._word = word
    
    # word = property(getWord)

    def match(self, words):
        matched = []
        for word in words:
            if sorted(word) == sorted(self.word):
                matched.append(word)
        return matched
