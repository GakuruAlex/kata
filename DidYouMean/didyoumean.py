class Dictionary:
    def __init__(self,words):
        self.words = words
    
    def find_most_similar(self,word):
        for element in self.words:
            if element.lower() == word.lower():
                return element
