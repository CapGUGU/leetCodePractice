class Solution(object):
    def canMakePaliQueries(s, queries):
        checklist = []  # the list of check list

        for left,right,replaceNum in queries:

            result = True
            while left <= right:
                if s[left] != s[right]:
                    if replaceNum <= 0:
                        result = False
                    else:
                        replaceNum -= 1
                left += 1
                right -= 1
            checklist.append(result)

        return checklist
    
s = "abcda"
queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
print(Solution.canMakePaliQueries(s,queries))