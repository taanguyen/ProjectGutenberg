from collections import defaultdict
import re

class TextAnalysis():
    def __init__(self, filepath):
        with open('./1000mostcommonwords.txt') as reader:
            common_words_text = reader.read()
            self.common_words = common_words_text.split()

        regex = re.compile('["$%*+-/:;<=>@^_,\.!?()]')
        self.words = []
        with open(filepath, 'r') as reader:
            book_text = reader.read()
            words_unfiltered = book_text.split()
            for word in words_unfiltered:
                # remove punctuation from word 
                word = regex.sub("", word)
                # remove whitespaces
                word = word.strip()
                self.words.append(word)

        self.word_count = defaultdict(int)
        for word in self.words:
            self.word_count[word if word == "I" else word.lower()] += 1
        self.word_count = list(self.word_count.items())

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
        return sorted(self.word_count, key=lambda wc: (-wc[1], wc[0]))[:20]

    def get20MostInterestingFrequentWords(self, limit = 100):
        # filters the most common 100 English words and 
        # returns the 20 most frequently used words 
        # and the number of times they were used
        common_set = set(self.common_words[:limit])
        most_interesting = list(filter(lambda x: x[0] not in common_set, self.word_count))
        most_interesting.sort(key=lambda wc: (-wc[1], wc[0]))
        return most_interesting[:20] 
    
    def get20LeastFrequentWords(self):
        # returns the 20 LEAST frequently used words 
        # and the number of times they were used
        return sorted(self.word_count, key=lambda x: (x[1], x[0]))[:20]

    def getFrequencyOfWord(self, word):
        #return an array of the number of the times the word was used in each chapter
        pass
        


    


                
