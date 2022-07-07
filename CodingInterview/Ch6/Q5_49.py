class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        for word in strs:
            word_list = list(word)
            word_list.sort()
            word_list = "".join(word_list)
            if word_list not in word_dict:
                word_dict[word_list] = [word]
            else:
                word_dict[word_list].append(word)

        ans = []
        for each in word_dict.values():
            each = list(each)
            ans.append(each)

        return ans