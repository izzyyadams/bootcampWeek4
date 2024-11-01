class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        knowingPeople = deque([[delay, forget]])
        for i in range(n):
            for j in range(len(knowingPeople)):
                if knowingPeople[j][0] == 0:
                    knowingPeople.append([delay,forget])
                else:
                    knowingPeople[j][0] -= 1
                if knowingPeople[j][1] == 0:
                    knowingPeople.popleft()
                else:
                    knowingPeople[j][1] -= 1
        return len(knowingPeople)
