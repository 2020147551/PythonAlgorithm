import collections
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = list(
        paragraph.replace('!', ' ').replace('?', ' ').replace("'", ' ').replace(';', ' ').replace(',', ' ').replace('.',
                                                                                                                    ' ').split())

        word_count = {}
        for word in paragraph:
            word = word.lower()
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        word_count = sorted(word_count.items(), key=lambda item: -item[1])

        for word in word_count:
            if word[0].lower() in banned:
                continue
            else:
                return word[0].lower()

#solution from the book
# def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#     words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
#
#     counts = collections.Counter(words)
#
#     return counts.most_common(1)[0][0]