'''
input:aaabbbca
output:abca


'''
def removeDuplicates(S):
  a=[]
  for i in S:
   if a and a[-1]==i:
    a.pop()
   else :
    a.append(i)
  return "".join(a)
print(removeDuplicates(input()))
