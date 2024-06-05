class Anagram:
    def __init__(self, word):
        self.word = word
        self.result = []
        self.characters = []
     
    def match(self, word_list):
        self.characters = [letter for letter in self.word]
        for element in word_list:
            element_chars = [letter for letter in element]
            if sorted(element_chars) == sorted(self.characters):
                self.result.append(element)
            else:
                continue
        return self.result