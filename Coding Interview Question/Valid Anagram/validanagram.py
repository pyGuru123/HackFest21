from random import randint
class Solution:
    def quicksort(self,array):
        if len(array) < 2:
            return array
        low, same, high = [], [], []
        pivot = array[randint(0, len(array) - 1)]
        for item in array:
            if item < pivot:
                low.append(item)
            elif item == pivot:
                same.append(item)
            elif item > pivot:
                high.append(item)
        return self.quicksort(low) + same + self.quicksort(high)

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = list(s)
        t = list(t)
        s = self.quicksort(s)
        t = self.quicksort(t)

        return s == t

ss = Solution()
print(ss.isAnagram("anagram","nagaram"))