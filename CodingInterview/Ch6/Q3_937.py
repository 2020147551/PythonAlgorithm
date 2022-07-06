class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []

        for log in logs:
            temp = log.split()
            back1 = ''.join(temp[1:])
            back2 = ' '.join(temp[1:])
            if back1.isdigit():
                digits.append(temp[0] + ' ' + ' '.join(list(back2.split())))
            else:
                letters.append(temp[0] + ' ' + ' '.join(list(back2.split())))

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits