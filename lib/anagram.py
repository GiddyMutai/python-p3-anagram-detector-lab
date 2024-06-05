class Anagram:
    def __init__(self, word):
        self.word = word
     
    def match(self, word_list):
        result = []
        characters = [letter for letter in self.word]
        for element in word_list:
            element_chars = [letter for letter in element]
            if sorted(element_chars) == sorted(characters):
                result.append(element)
            else:
                continue
        return result