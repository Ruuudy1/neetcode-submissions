class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # counter = dict()

        arr = list(zip(heights, names))
        arr.sort(reverse=True)
        return [name for _, name in arr]


        # for i in range(len(heights)):
        #     counter[heights[i]] = names[i]
        # return [value for key, value in sorted(counter.items(), reverse=True)]