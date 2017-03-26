class Stemmer:
    def __init__(self):
        from TurkishStemmer import TurkishStemmer
        self.stemmer = TurkishStemmer()
        pass

    def stem(self,text):
        words = text.split(" ")
        stemmed = ""
        for w in words:
            stemmed += self.stemmer.stem(w) + " "
        return stemmed.rstrip()
