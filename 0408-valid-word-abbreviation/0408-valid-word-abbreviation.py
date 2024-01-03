class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w, a = 0, 0
        
        while a < len(abbr) and w < len(word):
            if not abbr[a].isnumeric():
                if word[w] != abbr[a]:
                    return False
                a += 1
                w += 1
            else:
                if abbr[a] == '0':
                    return False
                j = a + 1
                while j < len(abbr) and abbr[j].isnumeric():
                    j += 1
                num = int(abbr[a:j])
                a = j
                w += (num)
                
        return True if a == len(abbr) and w == len(word) else False