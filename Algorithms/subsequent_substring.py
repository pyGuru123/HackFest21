
#Program to find length of substring with consecutive common characters 
#input:aaabbbccaaaa
#output:4
#expalination: we see that maximum i.e,4 times 'a' is repeated in complete string so answer is 4

#intution:

#1.We actually traverse through out the string and compare str[i] withh its next element str[i+1] .
#2.if we find that both elements are same then we increase our count variable else our count is set to maximum value till now which we have received.
#3.Finally we return our count variable which gives count of the maximum times the specific character is present.

class Solution:
   def solve(self, str):
      if len(str)==0:  #if input string is empty then return 0
         return 0
      str+=' '
      count=1  #initialize count variable ,it holds our maximum count which we need to return as output
      temp=1   #it holds the counting of that character for temporary time .once the next charactoer is different then we put it in 'count' variable and again initialize it to 1
      for i in range(len(str)-1):
         if str[i]==str[i+1]:
            temp+=1
         else:
            count=max(temp,count)
            temp=1
      return count  #returning our count as output
ob = Solution()
print(ob.solve("aaabbbccaaaa"))
