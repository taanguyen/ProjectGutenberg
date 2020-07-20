from collections import defaultdict
import re

class TextAnalysis():
    def __init__(self, filepath):
        with open('./1000mostcommonwords.txt') as reader:
            common_words_text = reader.read()
            self.common_words = common_words_text.split()
        
        # process text from book, line by line
        regex = re.compile('["$%*+-/:;<=>@^_,\.!?()]')
        self.words = []
        # store each chapter using the index of the chapter line
        self.chapters = []
        with open(filepath, 'r') as reader:
            self.lines = reader.readlines()
            for i in range(len(self.lines)):
                line = self.lines[i]
                # gutenberg books surround headings with 2 newlines on either side
                if i - 1 >= 0 and i + 1 < len(self.lines) and self.lines[i+1] == "\n" and self.lines[i-1] == "\n":
                    if i - 2 >= 0 and i + 2 < len(self.lines) and self.lines[i+2] == "\n" and self.lines[i-2] == "\n":
                        self.chapters.append(i)
                        #print(line)
                words_unfiltered = line.split()
                for word in words_unfiltered:
                    # remove punctuation from word 
                    word = regex.sub("", word)
                    # remove whitespaces
                    word = word.strip()
                    self.words.append(word)
            #print(self.chapters)
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
        chapter_idx = 0
        chapter_frequency = defaultdict(int)
        for index in range(len(self.lines)):
            line = self.lines[index]
            # parse each line of current chapter 
            for word_text in line.split():
                if word_text.lower() == word.lower():
                    chapter_frequency[chapter_idx] += 1 
            if chapter_idx < len(self.chapters) and index == self.chapters[chapter_idx]:
                # we have reached the start of a new chapter
                chapter_idx += 1 
        print(len(self.chapters))
        for chapter in self.chapters:
            if self.lines[chapter].istitle():
                print(self.lines[chapter])
        #print([self.lines[i] for i in self.chapters])
        return list(chapter_frequency.values())

    


                
