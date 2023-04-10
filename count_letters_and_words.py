
class Count:
    def count_letters(self, word):
        word = word.lower()
        result = {}
        for letter in word:
            if letter in result:
                    result[letter] += 1                
            else:
                result[letter] = 1
        return result

    def count_words(self, words):
        words_dict = {}
        words_list = words.split(' ')
        for word in words_list:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
        return words_dict

    