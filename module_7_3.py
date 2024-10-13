
class WordsFinder:

    def __init__(self, *args):
        self.file_names = []
        for name in args:
            self.file_names.append(name)

    def get_all_words(self):
        simv = [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_words = {}
        for file in self.file_names:
            with open(file, encoding='utf-8') as file_:
                text = file_.read().lower()
                for sim in simv:
                    text = text.replace(sim, '')
                all_words[file] = text.split()
        return all_words

    def find(self, word):
        res = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            for wrd in words:
                if wrd.upper() == word.upper():
                    res[name] = words.index(wrd) + 1
        return res

    def count(self, word):
        res = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            i = 0
            for wrd in words:
                if wrd.upper() == word.upper():
                    i += 1
            res[name] = i
        return res

if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words()) # Все слова

    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
