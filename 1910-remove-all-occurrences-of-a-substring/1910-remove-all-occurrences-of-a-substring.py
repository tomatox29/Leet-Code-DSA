class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, "", 1)
        return s 


#second approach using stack 
        stack=[]
        part_len=len(part)


        for ch in s:
            stack.append(ch)

            if len(stack)>= part_len and "".join(stack[-part_len:])==part:
                del stack[-part_len:]

            result="".join(stack)
        return result



        
  


   

         