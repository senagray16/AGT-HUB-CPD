class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        a = {}
        for i in list1:
            if i in list2:
                b = list1.index(i) + list2.index(i)
                if b not in a:
                    a[b] = [i,]
                else:
                    a[b].append(i)

        d = min(a.keys())
        return a[d]
