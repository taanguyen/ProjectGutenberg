from collections import defaultdict

class TextAnalysis():
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as reader:
            self.text = reader.read()
            self.words = self.text.split()

    def getTotalNumberOfWords(self):
        # return the number of words in the file.
        return len(self.words)


    def getTotalUniqueWords(self):
        # returns the number of UNIQUE words in the novel
        unique_words = set()
        for word in self.words:
            if word.lower() not in unique_words:
                unique_words.add(word.lower())
        return unique_words
    
    def get20MostFrequentWords(self):
        # return the 20 most frequently used words
        # in the novel and the number of times they were used
        word_count = defaultdict(int)
        for word in self.words:
            word_count[word.lower()] += 1 
        word_count_list = list(word_count.items())
        word_count_list.sort(key=lambda wc: (wc[1], wc[0]))
        return word_count_list[:20]

    def get20MostInterestingFrequentWords():
        pass


    


                
