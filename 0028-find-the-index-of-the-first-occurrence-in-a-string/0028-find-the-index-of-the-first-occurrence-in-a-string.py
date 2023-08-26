class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Rabin-Karp Algo
        lenHaystack, lenNeedle = len(haystack), len(needle)

        # initial checks
        if needle == "":
            return 0
        if lenNeedle > lenHaystack:
            return -1
        
        hashString, hashPattern = 0, 0 
        for i in range(lenNeedle):
            # calculate the needle hash and initial haystack hash
            hashString += ord(haystack[i])
            hashPattern += ord(needle[i])
            
        start, end = 0, lenNeedle 
        for index in range(lenHaystack - lenNeedle + 1): 
            if hashString == hashPattern:
                # if hash matches, compare the values 
                if haystack[start:end] == needle: 
                    return index 
                
            if end <= lenHaystack-1: 
                hashString -= ord(haystack[start]) 
                hashString += ord(haystack[end])
                start += 1
                end += 1

        return -1