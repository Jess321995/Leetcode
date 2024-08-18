class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Time Complexity: O(2^n). 
        # Auxiliary Space: O(n). 
        # The space complexity can be reduced to O(n) if global variable
        # or static variable is used to store the output string.
        output = []
        def helper(o, c, res):
            if o == 0 and c == 0:
                output.append(res)
                return 
            if o > 0:
                helper(o - 1, c, res + "(")
            if o < c:
                helper(o, c - 1, res + ")")
        helper(n, n, "")
        return output