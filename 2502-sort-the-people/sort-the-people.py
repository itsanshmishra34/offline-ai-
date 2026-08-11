class Solution:
    def sortPeople(self, names, heights):
        people = list(zip(heights, names))
        people.sort(reverse=True)

        return [name for height, name in people]