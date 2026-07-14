class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        j=0

        for num in range(1,n+1):
            if num == target[j]:
                ans.append("Push")
                j+=1

                if j == len(target):
                    break
                    
            else:
                ans.append("Push")
                ans.append("Pop")

        return ans


